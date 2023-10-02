# 🛠️ Are Copilots Local Yet?

Current trends and state of the art for using open & local LLM models as copilots to complete code, generate projects, act as shell assistants, automatically fix bugs, and more.

📝 *Help keep this list relevant and up-to-date by [making edits][edit]!*

[edit]: https://github.com/ErikBjare/are-copilots-local-yet/edit/master/README.md

## 📋 Summary

Local Copilots are in an early experimental stage, with most being of MVP-quality. 

The reasons for this are:

- 📉 Local models still being inferior to Copilot
- 🔧 Difficult to set up
- 💻 High hardware requirements

However, as models improve, and editor extensions get developed to use them, we're expected to get a renaissance of code-completion tools.

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

## 🧩 Extensions

Editor extensions used to complete code using LLMs:

| Name                            | Editor      | :star:  | Released  | Notes                                               |
| -------------                   | --------    | ------- | --------  | ---------                                           |
| [GitHub Copilot][copilot-vim]   | VSCode, vim | Many    | 2021-6-29 | The GitHub Original, not local or open-source.      |
| [Cursor][cursor]                | VSCode      | >17k    | 2023-3-14 | Fork of VSCode, not open-source                     |
| [Fauxpilot][fauxpilot]          | VSCode      | >12k    | 2022-9-3  | Early local PoC. Stale?                             |
| [Tabby][tabby]                  | VSCode      | >8k     | 2023-9-30 | Completes the cursor selection                      |
| [turbopilot][turbopilot]        | VSCode      | >3k     | 2023-4-10 | Completions with FIM support, inspired by fauxpilot |
| [HuggingFace-vscode][hf-vscode] | VSCode      | >300    | 2023-6-19 | Fork of Tabnine, supports Starcoder                 |
| [localpilot][localpilot] | VSCode      | >140    | 2023-10-2 |                  |
| [StarcoderEx][sc-ex]            | VSCode      | >60     |           | Completes the cursor selection                      |
| [WizardCoder-VSC][wc-vsc]       | VSCode      | >50     |           | PoC, [article][wc-vsc-blog]                         |

[copilot-vim]: https://github.com/github/copilot.vim
[cursor]: https://github.com/getcursor/cursor
[fauxpilot]: https://github.com/fauxpilot/fauxpilot
[tabby]: https://github.com/TabbyML/tabby
[hf-vscode]: https://github.com/huggingface/huggingface-vscode
[sc-ex]: https://github.com/Lisoveliy/StarCoderEx
[wc-vsc]: https://github.com/mzbac/wizardCoder-vsc
[wc-vsc-blog]: https://medium.com/@anchen.li/build-your-own-copliot-using-open-source-llm-ff9da556cb09
[turbopilot]: https://github.com/ravenscroftj/turbopilot
[localpilot]: https://github.com/danielgross/localpilot

## 🛠️ Tools

Tools that try to generate projects/features from specification:

| Name                         | :star:  | Released  | Notes                                                                                                                |
| --------------               | ------- | --------- | -----                                                                                                                |
| [gpt-engineer][gpt-engineer] | >42k    | 2023-6-6  | Specify what you want it to build, the AI asks for clarification, and then builds it.                                |
| [gpt-pilot][gpt-pilot]       | >4k     | 2023-7-18 | Very similar to gpt-engineer                                                                                         |
| [continue][continue]         | >4k     | 2023-5-24 | VSCode extension. Task-based autocomplete                                                                            |
| [aider][aider]               | >3k     | 2023-6-8  | AI pair programming in your terminal, "works well with pre-existing, larger codebases"                               |
| [rift][rift]                 | >2k     | 2023-6-20 | VSCode extension. Lets you write code by chatting, "makes your IDE agentic", "AI engineer that works alongside you". |
| [mentat][mentat]             | >1k     | 2023-7-25 | Mentat coordinates edits across multiple locations and files.                                                        |
| [clippinator][clippinator]   | >200    | 2023-4-15 | Uses a team of agents to plan, write, debug, and test                                                                |

[gpt-engineer]: https://github.com/AntonOsika/gpt-engineer
[gpt-pilot]: https://github.com/Pythagora-io/gpt-pilot
[continue]: https://github.com/continuedev/continue
[rift]: https://github.com/morph-labs/rift
[mentat]: https://github.com/biobootloader/mentat
[clippinator]: https://github.com/ennucore/clippinator
[aider]: https://github.com/paul-gauthier/aider

## 🗨️ Chat Interfaces

Chat interfaces with shell/REPL/notebook access. 
Similar to/inspired by ChatGPT's "Advanced Data Analysis" feature (previously "Code Interpreter").

| Name                     | :star:  | Notes                                                                                                  |
| --------------           | ------- | ---------                                                                                              |
| [open-interpreter][oi]   | >14k    | "open-source, locally running implementation of OpenAI's Code Interpreter"                             |
| [gptme][gptme]           | >80     | Supporting open models. Developed by me, @ErikBjare                                                    |
| [octogen][octogen] | >40 | Local Code Interpreter executing in Docker environment. |
| [terminal-x][terminal-x] | >30     | Very early prototype that converts natural language into shell commands, unmaintained since Sept. 2021 |

[oi]: https://github.com/KillianLucas/open-interpreter
[gptme]: https://github.com/ErikBjare/gptme
[terminal-x]: https://github.com/davidfant/terminal-x
[octogen]: https://github.com/dbpunk-labs/octogen

## 🤖 Models

Models relevant for local Copilot-use. Ordered by most recent first.

| Name                            | Size       | Languages   | :star:  | Released   | Notes                                                                    |
| ------------------------------- | ---------- | ----------- | ------- | ---------- | -------                                                                  |
| [Phind CodeLlama v2][phind2]    | 34B        | Many        | >400    | 2023-8-27  |                                                                          |
| [WizardCoder-Python][wc-py]     | 7/13/34B   | Python      | >500    | 2023-8     |                                                                          |
| [CodeLlama][codellama]          | 7/13/34B   | Many        | >2k     | 2023-8     |                                                                          |
| [WizardCoder][wc-v1]            | 15B        | 80+         | >390    | 2023-6     | Fine-tuning of Starcoder                                                 |
| [replit-glaive][replit-glaive]  | 3B         | 1?          | >70     | 2023-7     | Small model fine-tuned on high-quality data with impressive performance. |
| [Starcoder][starcoder]          | 15B        | 80+         | >5k     | 2023-5     |                                                                          |
| [replit-v1-3b][replit-v1]       | 3B         | 20+         | >600    | 2023-5     |                                                                          |

[codellama]: https://github.com/facebookresearch/codellama
[starcoder]: https://github.com/bigcode-project/starcoder
[wc-py]: https://huggingface.co/WizardLM/WizardCoder-Python-34B-V1.0
[wc-v1]: https://huggingface.co/WizardLM/WizardCoder-15B-V1.0
[replit-v1]: https://huggingface.co/replit/replit-code-v1-3b
[replit-glaive]: https://huggingface.co/sahil2801/replit-code-instruct-glaive
[phind2]: https://huggingface.co/Phind/Phind-CodeLlama-34B-v2

**Note:** due to the pace of new model releases, this section is doomed to be out of date.

## 📰 Misc

- 🐦 [Tweet announcing this repo][announce]

[announce]: https://twitter.com/ErikBjare/status/1681616666600394753

## 📈 Stats

Stargazers over time:

[![Stargazers over time](https://starchart.cc/ErikBjare/are-copilots-local-yet.svg)](https://starchart.cc/ErikBjare/are-copilots-local-yet)
