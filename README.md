<!--

Hey, you!
Are you reading this in the generated README.md? Then you're in the wrong place!

The template and data used to generate the README is in `README.md.in` and `data.json`, respectively.

The README.md is generated using the following command: python3 generate_readme.py

-->

# 🛠️ Are Copilots Local Yet?

Current trends and state of the art for using open & local LLM models as copilots to complete code, generate projects, act as shell assistants, automatically fix bugs, and more.

📝 *Help keep this list relevant and up-to-date by [making edits][edit]!*

[edit]: https://github.com/ErikBjare/are-copilots-local-yet/edit/master/data/data.yaml

## Table of Contents

- [Summary](#-summary)
- [Background](#-background)
- [Completion](#-completion)
- [Editor Agents](#-editor-agents)
- [IDEs](#-ides)
- [CLI Agents](#-cli-agents)
- [Autonomous](#-autonomous)
- [Chat Interfaces](#-chat-interfaces)
- [Runtimes](#-runtimes)
- [Other](#-other)
- [Models](#-models)
- [Datasets](#-datasets)
- [Suggested Setup](#-suggested-setup)
- [History](#-history)
- [Stats](#-stats)

## 📋 Summary

Local Copilots are now fully functional, although with output quality still not on par with those offered by cloud-based services like GitHub Copilot.

This document is a curated list of local Copilots, shell assistants, and related projects. It is intended to be a resource for those interested in a survey of the existing tools, and to help developers discover the state of the art for projects like these.

## 📚 Background

In 2021, GitHub released Copilot which quickly became popular among devs. Since then, with the flurry of AI developments around LLMs, local models that can run on consumer machines have become available, and it has seemed only a matter of time before Copilot will go local.

Many perceived limitations of GitHub's Copilot are related to its closed and cloud-hosted nature.

As an alternative, local Copilots enable:

- 🌐 Offline & private use
- ⚡ Improved responsiveness
- 📚 Better project/context awareness
- 🎯 The ability to run models specialized for a particular language/task
- 🔒 [Constraining the LLM output](https://twitter.com/ErikBjare/status/1656731582001020928) to fit a particular format/syntax.


## 🧩 Completion

Editor extensions and servers that complete code using LLMs:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [GitHub Copilot](https://github.com/github/copilot.vim) | vscode, vim | 9125 | 2021-06-29 | The GitHub Original, not open-source. Local models (Ollama, BYOK) supported in VS Code chat. |
| [Fauxpilot](https://github.com/fauxpilot/fauxpilot) | vscode | 14645 | 2022-09-03 | Early local PoC. Stale? |
| [Tabby](https://github.com/TabbyML/tabby) | vscode, vim, jetbrains | 29074 | 2023-09-30 | Completes the cursor selection |
| [turbopilot](https://github.com/ravenscroftj/turbopilot) | vscode | 3818 | 2023-04-10 | Completions with FIM support, inspired by fauxpilot |
| [Llama Coder](https://github.com/ex3ndr/llama-coder) | vscode |  | 2023-11-21 | Uses Ollama |
| [HuggingFace-vscode](https://github.com/huggingface/huggingface-vscode) | vscode | 1255 | 2023-06-19 | Fork of Tabnine, supports Starcoder |
| [StarcoderEx](https://github.com/Lisoveliy/StarCoderEx) | vscode | 101 | 2023-05-05 | Completes the cursor selection |
| [WizardCoder-VSC](https://github.com/mzbac/wizardCoder-vsc) | vscode | 145 | 2023-06-19 | PoC, article available |
| [KoboldAIConnect](https://github.com/Phiality-dot/KoboldAIConnect-VSCODE) | vscode |  | 2023-10-07 | Copilot clone using local KoboldAI backend |
| [twinny](https://github.com/rjmacarthy/twinny) | vscode | 3279 | 2024-01-24 | The most no-nonsense locally hosted AI code completion plugin for VS Code |
| [LocalCompletion](https://github.com/lufixSch/LocalCompletion) | vscode | 27 | 2023-11-15 | Inline completion with support for any OpenAI compatible backend |

## 💬 Editor Agents

Chat and agent extensions inside your editor:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [continue](https://github.com/continuedev/continue) | vscode, jetbrains | 21966 | 2023-05-24 | VSCode & JetBrains extension with chat, tab-autocomplete, and actions. |
| [wingman](https://github.com/nvms/wingman) | vscode |  | 2023-12-06 | Prompts. Presets. Modes. |
| [uniteai](https://github.com/freckletonj/uniteai) | vscode, emacs, lsp | 309 | 2023-08-27 |  |
| [Privy](https://github.com/srikanth235/privy) | vscode | 916 | 2024-01-08 | A privacy-first coding assistant. |
| [gen.nvim](https://github.com/David-Kunz/gen.nvim) | vim | 1323 | 2023-10-01 | Edit selection using custom prompts |
| [rift](https://github.com/morph-labs/rift) |  | 3051 | 2023-06-20 | VSCode extension. Lets you write code by chatting, makes your IDE agentic, AI engineer that works alongside you. |
| [Refact.AI](https://github.com/smallcloudai/refact) |  | 1660 | 2023-10-06 | Full self-hostable code completion, chat and training service, complete with VSCode extension. |

## 🖥️ IDEs

Editors with built-in LLM support:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [Cursor](https://github.com/getcursor/cursor) | vscode | 27112 | 2023-03-14 | Fork of VSCode, not open-source |

## ⌨️ CLI Agents

Terminal-based coding agents:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [aider](https://github.com/paul-gauthier/aider) |  | 25618 | 2023-06-08 | AI pair programming in your terminal, works well with pre-existing, larger codebases |
| [gptme](https://github.com/ErikBjare/gptme) |  | 3131 |  | Supporting open models. Developed by me, @ErikBjare |
| [mentat](https://github.com/biobootloader/mentat) |  | 2583 | 2023-07-25 | Mentat coordinates edits across multiple locations and files. |

## 🛠️ Autonomous

Tools that try to generate projects/features from specification:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [gpt-engineer](https://github.com/AntonOsika/gpt-engineer) |  | 52940 | 2023-06-06 | Specify what you want it to build, the AI asks for clarification, and then builds it. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) |  | 32250 | 2023-07-18 | Very similar to gpt-engineer |
| [clippinator](https://github.com/ennucore/clippinator) |  | 364 | 2023-04-15 | Uses a team of agents to plan, write, debug, and test |

## 🗨️ Chat Interfaces

Chat interfaces with shell/REPL/notebook access.
Similar to/inspired by ChatGPT's "Advanced Data Analysis" feature (previously "Code Interpreter").

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) |  | 57982 |  | open-source, locally running implementation of OpenAI's Code Interpreter |
| [octogen](https://github.com/dbpunk-labs/octogen) |  | 256 |  | Local Code Interpreter executing in Docker environment. |
| [terminal-x](https://github.com/davidfant/terminal-x) |  | 34 |  | Very early prototype that converts natural language into shell commands, unmaintained since Sept. 2021 |
| [DODA](https://github.com/agentcasa/doda) |  |  |  | Electron based GUI for a local OpenAI Dev Assistant |

## ⚙️ Runtimes

Local model servers:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [ollama](https://github.com/jmorganca/ollama) |  | 111009 | 2023-08-27 | Easily get up and running with large language models locally. |

## 🧰 Other

Misc relevant useful tools:

| Name | Editors | :star: | Released | Notes |
| ---- | ------- | ------ | -------- | ----- |
| [localpilot](https://github.com/danielgross/localpilot) | vscode | 3369 | 2023-10-02 | Utility for easily hosting models locally, for use with official Copilot extension using custom API endpoint. |
| [Clipboard Conqueror](https://github.com/aseichter2007/ClipboardConqueror) |  |  | 2023-12-29 | Copy-paste copilot alternative usable from any editor. No autocomplete, no integration; manual context management made easy. |

## 🤖 Models

Models relevant for local Copilot-use. Ordered by most recent first.

| Name                            | Size       | Languages   | :star:  | Released   | Notes   |
| ------------------------------- | ---------- | ----------- | ------- | ---------- | ------- |
| [Phind CodeLlama v2](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2) | 34B | Many | 829 | 2023-08-27 |  |
| [WizardCoder-Python](https://huggingface.co/WizardLM/WizardCoder-Python-34B-V1.0) | 7/13/34B | Python | 765 | 2023-08 |  |
| [CodeLlama](https://github.com/facebookresearch/codellama) | 7/13/34B | Many | 16165 | 2023-08 |  |
| [WizardCoder](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0) | 15B | 80+ | 750 | 2023-06 | Fine-tuning of Starcoder |
| [replit-glaive](https://huggingface.co/sahil2801/replit-code-instruct-glaive) | 3B | 1? | 88 | 2023-07 | Small model fine-tuned on high-quality data with impressive performance. |
| [Starcoder](https://github.com/bigcode-project/starcoder) | 15B | 80+ | 7351 | 2023-05 |  |
| [replit-v1-3b](https://huggingface.co/replit/replit-code-v1-3b) | 3B | 20+ | 724 | 2023-05 |  |
| [SantaCoder](https://huggingface.co/bigcode/santacoder) | 1.1B | Python, Java, JavaScript | 331 | 2023-04 | Tiny model selectively trained on 3 languages from 'The Stack' |
| [Qwen 2.5 Coder](https://github.com/QwenLM/Qwen2.5-Coder) | 32b | 92 different languages | 3998 | 2024-11 |  |
| [Deepseek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 671B | Many | 3052 | 2025-01 |  |


**Note:** due to the pace of new model releases, this section is doomed to be out of date.

## 📚 Datasets

Datasets relevant for training models.

| Name                            | Size       | Languages   | :star:  | Released   | Notes   |
| ------------------------------- | ---------- | ----------- | ------- | ---------- | ------- |
| [The Stack](https://huggingface.co/datasets/bigcode/the-stack) | 3TB/6TB | 358 | 760 | 2022-10 | Excludes weak-copyleft licenses (MPL, LGPL, EGL) since v1.1 |


## Suggested setup

As you can see above there are many options for models and editor extensions. If you use VS Code or JetBrains and want to get started straight away you can use the following setup:

1. Install [LM Studio](https://lmstudio.ai/).
2. Install [Continue.dev](https://www.continue.dev/) extension.
3. Download one or several models in LM Studio. As of January 2025, Qwen 2.5 Coder is a good choice for autocomplete and Deepseek R1 is a good choice for chat. Depending on your hardware you'll have to experiment with which model size and quantization level gives you sufficient speed. For example on a Macbook Pro M2 with 32GB RAM, `Qwen2.5-Coder-7B-Instruct-Q4_K_M` works well for autocomplete and `DeepSeek-R1-Distill-Qwen-14B-Q4_0` works well for chat.
4. Go to the Developer tab in LM Studio and start the server.
5. Configure Continue.dev extension with by adding your selected models. For example:
    ```json
    {
        "models": [
            {
            "apiBase": "http://localhost:1234/v1/",
            "title": "Deepseek R1",
            "model": "bartowski/deepseek-r1-distill-qwen-14b",
            "provider": "lmstudio"
            }
        ],
        "tabAutocompleteModel": {
            "provider": "lmstudio",
            "apiBase": "http://localhost:1234/v1/",
            "title": "Qwen 2.5 Coder",
            "model": "qwen2.5-coder-7b-instruct"
        },
    }

## 📰 History

- 🐦 [Tweet announcing this repo][announce]

[announce]: https://twitter.com/ErikBjare/status/1681616666600394753

## 📈 Stats

Stargazers over time:

[![Stargazers over time](https://starchart.cc/ErikBjare/are-copilots-local-yet.svg)](https://starchart.cc/ErikBjare/are-copilots-local-yet)