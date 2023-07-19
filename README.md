# Are code copilots local yet?

The current state of using local LLM models to complete code.

*Help keep this list relevant and up-to-date by [making edits](https://github.com/ErikBjare/are-copilots-local-yet/edit/master/README.md)!*


## Summary

Local Copilots are in an early experimental stage, with most being of MVP-quality.

This is in part due to the local models still being inferior to Copilot. They can also be difficult to set up, and have high hardware requirements. However, as models improve, and editor extensions get developed to use them, we're expected to get a renaissance of code-completion tools.


## Extensions

Editor extensions used to complete code using LLMs:

| Name        | Editor | Stars | Notes   |
|-------------|--------|-------|---------|
| [Fauxpilot][fauxpilot]   | VSCode | >12k  | Stale?  |
| [HuggingFace][hf-vscode] | VSCode | >300  | Fork of Tabnine, supports Starcoder |
| [StarcoderEx][sc-ex] | VSCode | >60   | Completes the cursor selection |
| [WizardCoder VSC][wc-vsc] | VSCode | >50   | PoC, [article][wc-vsc-blog] |

[fauxpilot]: https://github.com/fauxpilot/fauxpilot
[hf-vscode]: https://github.com/huggingface/huggingface-vscode
[sc-ex]: https://github.com/Lisoveliy/StarCoderEx
[wc-vsc]: https://github.com/mzbac/wizardCoder-vsc
[wc-vsc-blog]: https://medium.com/@anchen.li/build-your-own-copliot-using-open-source-llm-ff9da556cb09

## Models

Models relevant for local Copilot-use:

| Name        | Size | Languages | Stars | Notes |
|-------------|------|-----------|-------|-------|
| [Starcoder][starcoder]   | 15B | 80+        | >5k   |       |
| [Wizardcoder][wc-v1] | 15B | 80+        | >390  | Fine-tuning of Starcoder |
| [replit-v1-3b][replit-v1] | 3B | 20+        | >600  |       |
| [replit-glaive][replit-glaive] | 3B | 1?        | >70   | Small model fine-tuned on high-quality data, with impressive performance. |

You can find more models and benchmarks at: [abacaj/code-eval][code-eval].

[starcoder]: https://github.com/bigcode-project/starcoder
[wc-v1]: https://huggingface.co/WizardLM/WizardCoder-15B-V1.0
[replit-v1-3b]: https://huggingface.co/replit/replit-code-v1-3b
[replit-glaive]: https://huggingface.co/sahil2801/replit-code-instruct-glaive
[code-eval]:https://github.com/abacaj/code-eval

## Background

In 2021, GitHub released Copilot which quickly became popular among devs. Since then, with the flurry of AI developments around LLMs, local models that can run on consumer machines have become available, and it has seemed only a matter of time before Copilot will go local.

Many perceived limitations of GitHub's Copilot are related to its closed and cloud-hosted nature. 

As an alternative, local Copilots enable:

- offline & private use.
- improved responsiveness.
- the ability to run models specialized for a particular language/task.
- [constraining the LLM output](https://twitter.com/ErikBjare/status/1656731582001020928) (using things like regular expressions) to fit a particular format/syntax.
