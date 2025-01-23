# LLM - Azure OpenAI Zero-Shot Prompting
This custom step helps you interact with a Large Language Model (LLM) interacting with an [Azure OpenAI](https://microsoftlearning.github.io/mslearn-openai/Instructions/Exercises/01-get-started-azure-openai.html) service to process simple instructions on specified input data. It uses a technique called zero-shot prompting which is useful for cases where the instruction provided to the LLM does not require additional detail or context.  

There exist both simple and involved (e.g. Retrieval Augmented Generation (RAG)) approaches for interacting with an LLM. Zero-shot prompting is useful for cases where the input data provides all the necessary context and information required for the LLM to process an instruction, and also, the instruction provided does not require a query to other data sources.  

Run inside a SAS session, this custom step takes either a SAS dataset or a CAS table as input and returns a SAS dataset (or CAS table) as output, with the response added as a new variable.

## A general idea

----
## Table of Contents

----
## Requirements

-----
## Parameters

-----
## Run-time Control
Note: Run-time control is optional.  You may choose whether to execute the main code of this step or not, based on upstream conditions set by earlier SAS programs.  This includes nodes run prior to this custom step earlier in a SAS Studio Flow, or a previous program in the same session.

Refer this blog (https://communities.sas.com/t5/SAS-Communities-Library/Switch-on-switch-off-run-time-control-of-SAS-Studio-Custom-Steps/ta-p/885526) for more details on the concept.
The following macro variable,
```sas
_azp_run_trigger
```
will initialize with a value of 1 by default, indicating an 'enabled' status and allowing the custom step to run.
If you wish to control execution of this custom step, include code in an upstream SAS program to set this variable to 0.  This 'disables' execution of the custom step.
To 'disable' this step, run the following code upstream:
```sas
%global _azp_run_trigger;
%let _azp_run_trigger = 0;
```
To 'enable' this step again, run the following (it's assumed that this has already been set as a global variable):
```sas
%let _azp_run_trigger = 1;
```

IMPORTANT: Be aware that disabling this step means that none of its main execution code will run, and any  downstream code which was dependent on this code may fail.  Change this setting only if it aligns with the objective of your SAS Studio program.

-----
## Documentation

-----
## SAS Program

Refer [here]() for the SAS program used by the step.  You'd find this useful for situations where you wish to execute this step through non-SAS Studio Custom Step interfaces such as the [SAS Extension for Visual Studio Code](https://github.com/sassoftware/vscode-sas-extension), with minor modifications.

-----
## Installation & Usage

- Refer to the [steps listed here](https://github.com/sassoftware/sas-studio-custom-steps#getting-started---making-a-custom-step-from-this-repository-available-in-sas-studio).
----
## Created/contact:

- [Sundaresh Sankaran](sundaresh.sankaran@sas.com)
- [Crystal Baker](crystal.baker@sas.com)

----
## Change Log
* Version 1.0.0(17JAN2025)
    - Initial version