# Github Copilot - General

* Create the File: In the root of your repository, create a file named `.github/copilot-instructions.md`. If the .github directory does not exist, create it first.
* Add Instructions: Add natural language instructions to the file in Markdown format. These instructions should be short, self-contained statements that add context or relevant information to supplement users' chat question

```md
# Copilot Instructions
This project is built with .NET 8, C# 12.0, and SQL Server, and is hosted in Azure.

## Coding Standards

- Use Allman style braces, where each brace begins on a new line. A single-line statement block can go without braces, but the block must be properly indented on its own line and must not be nested in other statement blocks that use braces.
- Use _camelCase for internal and private fields and use readonly where possible. Prefix internal and private instance fields with _, static fields with s_.
- Use camelCase for method parameters and local variables.
- Public fields should be used sparingly and should use PascalCase with no prefix when used.
- Use PascalCase to name all our constant local variables and fields.
- Use PascalCase for all method names, including local functions.
- Always specify the visibility, even if it's the default (e.g., private string _foo not string _foo). Visibility should be the first modifier (e.g., public abstract not abstract public).
- Only use var when the type is explicitly named on the right-hand side, typically due to either new or an explicit cast, e.g., var stream = new FileStream(...) not var stream = OpenStandardInput().
- Use language keywords instead of BCL types (e.g., int, string, float instead of Int32, String, Single, etc.) for both type references as well as method calls (e.g., int.Parse instead of Int32.Parse).
- Fields should be specified at the top within type declarations.
- Include XML documentation for all public methods, classes, and interfaces. For private methods, include inline comments where necessary to explain complex logic.

## Custom Instructions

- This project targets .NET 8 and uses C# 12.0. Ensure that all generated code is compatible with these versions.
- Ensure that all generated code adheres to the project's coding standards, including naming conventions, brace styles, the use of `var` and XML documentation

```