import abc
import copy

from model import Module
from util import replace_word


class Resolver(abc.ABC):
    """An abstract base class that defines the structure for resolver classes.

    Attributes:
        modules (list[Module]): A list of Module objects that contain documentation information.
    """

    modules: list[Module]

    def __init__(self, modules: list[Module]):
        """Initializes the Resolver with a list of modules.

        Args:
            modules (list[Module]): A list of modules containing documentation information.
        """
        self.modules = modules

    def resolve(self, *args):
        """Abstract method to be implemented by subclasses to perform specific resolving operations.

        Args:
            *args: Variable length argument list.
        """
        return


class TypeAliasResolver(Resolver):
    """A resolver class that handles the resolving of type aliases within the documentation text."""

    def resolve(self, text):
        """Resolves type aliases in the provided text by replacing alias names with their actual values.

        Args:
            text (str): The text containing potential type aliases to be resolved.

        Returns:
            str: The text with type aliases resolved.
        """
        has_resolved_text: bool = False

        for module in self.modules:
            for var in module.variables:
                value = var.value
                if not value:
                    continue

                if var.name == text:
                    return self.resolve(value)

                original_text: str = copy.deepcopy(text)
                text = replace_word(text, var.name, value)

                has_resolved_text = has_resolved_text or (text != original_text)

        return self.resolve(text) if has_resolved_text else text


class CrossReferenceResolver(Resolver):
    """A resolver class that handles the resolving of cross-references within the documentation text.

    Attributes:
        type_alias_resolver (Resolver): An instance of the TypeAliasResolver to resolve type aliases in the text.
    """

    type_alias_resolver: Resolver

    def __init__(self, modules: list[Module]):
        """Initializes the CrossReferenceResolver with a list of modules and a type alias resolver.

        Args:
            modules (list[Module]): A list of modules containing documentation information.
        """
        super().__init__(modules)
        self.type_alias_resolver = TypeAliasResolver(modules)

    def resolve(self, text: str) -> str:
        """Resolves cross-references in the provided text by replacing class names with markdown links to their documentation.

        Args:
            text (str): The text containing potential class names to be cross-referenced.

        Returns:
            str: The text with cross-references resolved.
        """
        text = self.type_alias_resolver.resolve(text)

        for module in self.modules:
            for class_ in module.classes:
                reference = f"[{class_.name}]({class_.name}.md)"

                if class_.name == text:
                    return reference

                text = replace_word(text, class_.name, reference)

        return text
