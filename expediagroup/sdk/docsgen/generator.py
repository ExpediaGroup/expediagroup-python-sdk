import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import docspec
from helper import helpers
from model import Master, Module
from pydoc_markdown import Context, Loader
from render import MarkdownRenderer
from resolver import CrossReferenceResolver, Resolver


@dataclass
class ExpediaGroupDocumentationGenerator:
    """
    A class to generate documentation for the Expedia Group.

    Attributes:
        context (Context): The context for the documentation generation.
        loader (Loader): The loader to load the modules.
        modules (list[Module]): A list of modules for documentation generation.
        renderer (MarkdownRenderer): Renderer for generating documentation in Markdown format.
        templates_path (Path): The path to the templates used for documentation generation.
        helpers (dict[str, Any]): A dictionary of helper functions for documentation generation.
        resolvers (dict[str, Resolver]): A dictionary of resolvers for resolving cross-references.
        master_filename (str): The filename for the master documentation file.
    """

    context: Context
    loader: Loader
    modules: list[Module]
    renderer: MarkdownRenderer
    templates_path: Path
    helpers: dict[str, Any]
    resolvers: dict[str, Resolver]
    master_filename: str

    def __init__(
        self,
        context: Context,
        loader: Loader,
        templates_path: Path,
        master_filename: str = "index",
        helpers: dict[str, Any] = dict(),  # noqa
        resolvers: dict[str, Resolver] = dict(),  # noqa
    ):
        """
        Initializes the ExpediaGroupDocumentationGenerator.

        Args:
            context (Context): Context data that is passed to plugins when they are loaded.
            loader (Loader): The loader to load the modules.
            templates_path (Path): The path to the templates used for documentation generation.
            master_filename (str, optional): The filename for the master documentation file. Defaults to "index".
            helpers (dict[str, Any], optional): A dictionary of helper functions for documentation generation used in the `jinja2` modules.
            resolvers (dict[str, Resolver], optional): A dictionary of resolvers used in the `jinja2` modules.
        """
        self.context = context
        self.master_filename = master_filename
        self.loader = loader
        self.templates_path = templates_path
        self.helpers = helpers
        self.resolvers = resolvers

        self.__post_init__()

    def __post_init__(self):
        """
        Post-initialization method to initialize loader, modules, renderer, and other necessary attributes.
        """
        self.loader.init(context=self.context)
        self.modules = list(map(Module.from_, filter(lambda m: isinstance(m, docspec.Module), list(self.loader.load()))))
        self.__post_process_modules()

        cross_reference_resolver: Resolver = CrossReferenceResolver(modules=self.modules)

        self.resolvers.update({"cross_reference_resolver": cross_reference_resolver})
        self.helpers.update(helpers)

        self.renderer = MarkdownRenderer(
            modules=self.modules,
            templates_path=self.templates_path,
            helpers=self.helpers,
            resolvers=self.resolvers,
            master=Master.from_modules(copy.deepcopy(self.modules)),
            master_filename=self.master_filename,
        )

    def generate(self, output_path: Path):
        """
        Generates the documentation and writes it to the specified output path.

        Args:
            output_path (Path): The path where the generated documentation will be written to.
        """
        self.renderer.render(output_path=output_path)

    def __post_process_modules(self):
        """
        Post-processes the modules to sync submodules and remove modules with no classes and one or fewer submodules.
        """
        for index, _ in enumerate(self.modules):
            self.modules[index].sync_submodules(modules=self.modules)

        # Removes modules that have no classes along with 1 or less submodule
        self.modules = list(filter(lambda module: len(module.classes) or len(module.submodules) > 1, self.modules))
