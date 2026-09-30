---
name: docx-stdlib-workflows
description: "Create a DOCX or fill an existing template with Python stdlib when python-docx is unavailable."
---

# DOCX with Python stdlib

Choose the route first: **new document** or **existing template**. Never rebuild a template from scratch; never treat a new document as a template.

Do the smallest useful thing: change only the requested content, reuse existing document helpers, and keep template structure intact. Do not add a document framework or redesign formatting unless requested.

## New document

- Build a ZIP (`zipfile`, `ZIP_DEFLATED`) with `[Content_Types].xml`, `_rels/.rels`, `word/document.xml`, `word/styles.xml`, `word/_rels/document.xml.rels`, `docProps/core.xml`, and `docProps/app.xml`. Escape visible text with `xml.sax.saxutils.escape`.
- Define small run/paragraph/cell/table helpers. Set widths, cell shading/margins/borders, font and alignment explicitly; for wide tables use landscape section properties. Use fixed table grid widths and `<w:tblHeader/>` on rows that must repeat.
- Follow the repository's language requirements. Use a descriptive output name; never overwrite the source.

## Existing template

1. Inspect `word/document.xml` and map each placeholder to its actual `<w:t>` run(s). A placeholder may span runs or have its `[` in the preceding run. Inspect all variants, pronouns and unbracketed placeholders; do not assume one literal matches them all.
2. Replace only exact intended text, asserting the expected count for every replacement. XML-escape inserted text and handle typographic apostrophes. Match within text-run boundaries, not arbitrary substrings of XML. If split across runs, edit the mapped runs deliberately rather than flattening the document. Remove a paragraph only after uniquely identifying it.
3. Follow the template's highlighting convention; when yellow means **still needs input**, remove it only from confirmed final values and preserve or add it to uncertain/unfilled values. Compare remaining highlighted runs with an explicit expected list. Assert no unintended stale placeholders or ambiguous gender text remain; explicitly unresolved fields may stay. Never invent names, identity numbers or dates.
4. **Fail before writing** if any count, placeholder or highlight check fails. Rezip the original entries, preserving their content and metadata where possible, and replace only `word/document.xml`. Keep the original template untouched.

## Both routes: verification

- Assert `ZipFile(output).testzip() is None`; parse `word/document.xml` and `[Content_Types].xml` as XML. For a filled template, verify all other ZIP members' uncompressed bytes match the source.
- Extract/read the finished DOCX end-to-end: title, every table/paragraph, notes, Unicode and remaining placeholders. For a template, check the expected yellow-highlight set again in the *output*.
- Report artifact path and checks. Structural/XML/text validity does **not** prove Word layout: claim visual QA only after opening/rendering the file.
