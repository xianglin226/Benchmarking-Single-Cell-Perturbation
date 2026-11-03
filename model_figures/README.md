# Archived model diagrams

This folder contains **104 images for 96 of the 100 models** in the perturbation and scFM tables: 96 Figure 1 images and 8 additional architecture figures. Checked on 3 November 2026.

The **model structure** links in the [main table](../README.md) and [scFM table](../scFM/README.md) point to these files. A detailed architecture figure is preferred over a general Figure 1 overview when one has been archived. Architecture/type labels are deliberately brief; toolkits and statistical methods retain their own method-family labels.

- `*_Figure1.*`: the source paper's Figure 1.
- `*_Architecture_Figure2.*`: an additional Figure 2 showing the model or method framework; the original figure number is retained.
- [sources.json](sources.json): paper URLs, image URLs, figure numbers, original dimensions, extraction methods, and checksums. PDF page and crop coordinates are provided for PDF-derived images. Preprint-version notes are recorded per model.
- [structures.json](structures.json): the short labels, selected figure files, and supporting primary sources used by the tables.
- [missing.txt](missing.txt): **DTD, scPreGAN, scAgents, and CSTATE** currently have no archived figure because public downloads could not be retrieved and verified. Their table labels are plain text, with no placeholder image links.

Publisher/PMC/official-author images are preserved as downloaded. PDF-derived images are rendered and cropped from the original paper. Figure 1 is not always a neural-network architecture: the linked file may instead show a statistical method, an analysis workflow, or the paper's overview, as noted in the source manifest. The collection spans both predictive models and related methods retained in the tables.

The original authors and publishers retain ownership of their figures; source-paper licenses and attribution apply. No independent license is granted over these images. The local `index.html` gallery can be opened after downloading this folder; GitHub displays the README and individual image files directly.
