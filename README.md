Overview:



AI Creative Automation Engine is a lightweight cloud-based system for generating structured marketing campaign assets using generative AI.



It enables batch image generation, prompt variation, campaign organization, and experiment logging — designed to simulate internal creative tooling used by mobile gaming studios.



Problem It Solves:



Marketing teams need to generate multiple ad variations quickly for testing and iteration.



Manual workflows are:



Slow

Repetitive

Hard to scale



This system automates:



Prompt variation

Image generation

Campaign folder structuring

Metadata tracking

Non-technical UI access



Features:



Cloud-based Stable Diffusion integration (HuggingFace Inference API)

Prompt templating engine for variation testing

Batch campaign generation

Automatic campaign folder creation

CSV-based experiment logging

Streamlit UI for non-technical users



Architecture:



User Input (UI)

→ Prompt Engine (variation logic)

→ HuggingFace Inference API

→ Batch Generator

→ Campaign Folder Output

→ CSV Logging



Tech Stack:



Python

HuggingFace Inference API

Streamlit

Requests

Dotenv

CSV logging



Example Workflow



Enter campaign name

Enter base theme

Select number of variations

Click "Generate Campaign"

Images saved in /campaigns

Metadata logged in /logs/campaign\_log.csv



Why This Matters:



This project demonstrates:



Generative AI integration

Automation pipeline design

Prompt engineering strategy

Batch orchestration

Internal tooling mindset

Creative production scaling



Future Improvements



A/B experiment tracking dashboard

Model switching (multiple inference providers)

Auto-caption generation

Cloud storage integration

Performance metrics tracking

## Screenshots



\### UI

!\[UI](assets/ui.png)



\### Generated Campaign Output

!\[Campaign](assets/campaign\_output.png)



\### Experiment Logging

!\[Logs](assets/logs.png)

