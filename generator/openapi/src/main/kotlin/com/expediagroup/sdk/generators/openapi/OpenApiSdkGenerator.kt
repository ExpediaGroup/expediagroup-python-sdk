/*
 * Copyright (C) 2022 Expedia, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.expediagroup.sdk.generators.openapi

import com.github.rvesse.airline.SingleCommand
import com.github.rvesse.airline.annotations.Command
import com.github.rvesse.airline.annotations.Option
import org.openapitools.codegen.DefaultGenerator
import org.openapitools.codegen.api.TemplateDefinition
import org.openapitools.codegen.config.CodegenConfigurator
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.nio.file.Files
import java.util.Base64
import java.util.zip.ZipInputStream
import kotlin.io.path.writeBytes

/**
 * Configures the OpenAPI Generator based on command line parameters to generate an EG Travel SDK project
 * This will produce a maven project in the specified output directory
 */
@Command(name = "generate", description = "Let's build an EG Travel SDK!")
class OpenApiSdkGenerator {
    companion object {

        /**
         * Main Entry Point
         *
         * Parses command line arguments and then generates an EG Travel SDK
         */
        @JvmStatic
        fun main(args: Array<String>) {
            val generator = SingleCommand.singleCommand(OpenApiSdkGenerator::class.java).parse(*args)
            generator.run()
        }
    }

    @Option(name = ["-i", "--input-spec"])
    lateinit var inputFile: String

    @Option(name = ["-o", "--output-directory"])
    lateinit var outputDirectory: String

    @Option(name = ["-n", "--namespace"])
    lateinit var namespace: String

    @Option(name = ["-v", "--version"])
    lateinit var version: String

    fun run() {
        try {
            val config = CodegenConfigurator().apply {
                // Adjust namespace to fit with JVM package naming conventions
                val packageName = namespace.lowercase().replace(Regex("[^a-z0-9]"), "")
                // specify the target language
                setGeneratorName("python")
                setTemplateDir("templates/openworld-sdk/")
                setInputSpec(
                    prepareSpecFile()
                )
                setOutputDir(outputDirectory)
                // Configure CodeGen Components
                addGlobalProperty("models", "")
                addGlobalProperty("apis", "")
                addGlobalProperty("supportingFiles", "requirements.txt,setup.py,apis_tag_to_api.handlebars")

                // Configure generated client suffix eg: AnyNameClient
                setApiNameSuffix("Client")
                setModelPackage("model")
                setApiPackage("client")

                // Configure generated Enum class names
                addAdditionalProperty("enumPropertyNaming", "UPPERCASE")
                addAdditionalProperty("sortParamsByRequiredFlag", true)
                // Configure SDK Artifact Coordinates
                setArtifactVersion(version)
                setGroupId("openworld.sdk")
                setArtifactId("openworld-sdk-python-$packageName")
                // Configure package details
                setInvokerPackage("openworld.sdk")
                addAdditionalProperty("normalizedNamespace", "$packageName")
                addAdditionalProperty("projectName", "openworld.sdk.$packageName")
                addAdditionalProperty("namespace", "$namespace")
                setPackageName("openworld.sdk.$packageName")
            }
            // Load Template Customizations
            val generatorInput = config.toClientOptInput().apply {
                userDefinedTemplates(
                    listOf(
                        TemplateDefinition("requirements.handlebars", "requirements.txt")
                    )
                )
            }
            val generator = DefaultGenerator(false).apply { opts(generatorInput) }
            generator.generate()
        } catch (e: Exception) {
            System.err.println("Failed to generate SDK")
            System.err.println(e.message)
            e.printStackTrace()
        }
    }

    private fun prepareSpecFile(): String {
        val buffer = ByteArray(1024)
        val zipInputStream = ZipInputStream(FileInputStream(prepareTmpZipFile()))
        val tempFile = Files.createTempFile("", zipInputStream.nextEntry?.name).toFile()
        val fileOutputStream = FileOutputStream(tempFile)
        var len: Int
        while (zipInputStream.read(buffer).also { len = it } > 0) {
            fileOutputStream.write(buffer, 0, len)
        }
        zipInputStream.closeEntry()
        fileOutputStream.close()
        zipInputStream.close()
        return tempFile.absolutePath
    }

    private fun prepareTmpZipFile(): File {
        val tmpFile = Files.createTempFile("", "tmp")
        tmpFile.writeBytes(Base64.getDecoder().decode(inputFile))
        return tmpFile.toFile()
    }
}
