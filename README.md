# Are code copilots local yet?

The current state of using local LLM models to complete code.

***Help keep this list relevant and up-to-date my making pull requests!***

## Extensions

| Name        | Editor | Stars | Notes   |
|-------------|--------|-------|---------|
| [Fauxpilot][fauxpilot]   | VSCode | >12k  | Stale?  |
| [WizardCoder][wizardcoder-vsc] | VSCode | >50   | [article][https://medium.com/@anchen.li/build-your-own-copliot-using-open-source-llm-ff9da556cb09] |
| [HuggingFace][hf-vscode] | VSCode | >300 | Supports Starcoder
| [StarcoderEx][sc-ex] | VSCode | >60 | | Completes the cursor selection

[fauxpilot]: https://github.com/fauxpilot/fauxpilot
[wizardcoder-vsc]: https://github.com/mzbac/wizardCoder-vsc
[hf-vscode]: https://github.com/huggingface/huggingface-vscode
[sc-ex]: https://github.com/Lisoveliy/StarCoderEx

## Models

Some models relevant for local Copilot-use. You can find more and benchmarks at: https://github.com/abacaj/code-eval

| Name        | Size | Languages | Stars | Notes |
|-------------|------|-----------|-------|-------|
| [Starcoder][starcoder]   | 15B | 80+       | >5k   |
| [Wizardcoder][wc-v1] | 15B | 80+     | >390 | Fine-tuning of Starcoder
| [replit-code-instruct-glaive][] | 3B | 1? | >70 | Small model with impressive performance

[starcoder]: https://github.com/bigcode-project/starcoder
[wc-v1]: https://huggingface.co/WizardLM/WizardCoder-15B-V1.0
[replit-glaive]: https://huggingface.co/sahil2801/replit-code-instruct-glaive

## Background

In 2021, GitHub released Copilot which quickly became popular among devs. Since then, with the flurry of AI developments around LLMs, local models that can run on consumer machines have become available, and it has seemed only a matter of time before Copilot will go local.

Many perceived limitations of GitHub's Copilot are related to its closed and cloud-hosted nature. 

As an alternative, local Copilots enable:

- offline & private use
- the ability to run models specialized for a particular language/task.
- [constraining the LLM output](https://twitter.com/ErikBjare/status/1656731582001020928) (using things like regular expressions) to fit a particular format/syntax.
