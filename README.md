# Weave Monitor Test Script

A simple test script demonstrating how to use [W&B Weave Monitor](https://docs.wandb.ai/weave/guides/evaluation/guardrails_and_monitors) with custom parameters, including support for non-English parameter names.

## Overview

This script provides a minimal example for testing Weave's Monitor feature, which enables automated quality evaluation of LLM outputs using LLM-as-a-Judge scoring.

## Features

- ✅ Simple function decorated with `@weave.op()` for automatic tracing
- ✅ Support for Japanese parameter names (e.g., `文字数`)
- ✅ Clear documentation for available variables in Monitor scoring prompts
- ✅ Multiple test cases to demonstrate Monitor behavior

## Prerequisites

```bash
pip install weave
```

## Usage

### 1. Run the script

```bash
python simple_monitor_test.py
```

This will:
- Create traces in your Weave project
- Generate test summaries with different character counts (100, 200, 300)
- Display the results in the console

### 2. Create a Monitor in Weave UI

1. Navigate to your Weave project: https://wandb.ai/wandb/monitor-test-simple/weave
2. Go to the **Monitors** tab
3. Click **New Monitor**
4. Configure the monitor:
   - **Operations**: Select `generate_summary`
   - **Sampling rate**: `100%` (for testing)
   - **Judge model**: `gpt-4` (recommended; avoid `gpt-4o` due to API compatibility issues)
   - **System prompt**: 
     ```
     You are an expert at evaluating summary quality.
     ```
   - **Scoring prompt**: 
     ```
     Evaluate the following summary:
     
     Original text: {text}
     Target length: {文字数} characters
     Generated summary: {output}
     
     Rate the summary on a scale of 1-10 and provide reasoning.
     ```

### 3. View Results

- Check the **Traces** page to see your function calls
- Check the **Monitors** page to see evaluation scores (may take 2-5 minutes for async processing)

## Available Variables in Scoring Prompts

When configuring your Monitor's scoring prompt, you can reference:

| Variable | Description |
|----------|-------------|
| `{text}` | The input text parameter |
| `{文字数}` | The target character count parameter |
| `{output}` | The generated summary (function return value) |
| `{inputs}` | A JSON dictionary of all input parameters |

**Important**: Variable names must exactly match your function's parameter names!

## Key Learnings

This example demonstrates several important concepts:

1. **Parameter Naming**: Monitor variables must match function parameter names exactly
   - ✅ Correct: `{text}`, `{文字数}`, `{output}`
   - ❌ Incorrect: `{input}`, `{文字数}` (if parameter is named `char_count`)

2. **Model Compatibility**: Use `gpt-4` instead of `gpt-4o` for the Judge model
   - `gpt-4o` requires `max_completion_tokens` parameter
   - Weave currently uses `max_tokens` (compatibility issue)

3. **Async Processing**: Monitor scoring happens asynchronously
   - Expect 2-5 minute delay for results
   - This is by design for production scalability

4. **Non-English Parameters**: You can use Japanese, Chinese, or other non-English parameter names
   - Just ensure consistency between function signature and scoring prompt

## Troubleshooting

### Monitor not capturing calls
- Verify the Monitor is **Active** (toggle on)
- Check that **Operations** matches your function name exactly
- Wait 60 seconds after configuration changes (cache refresh period)

### Scoring failures (KeyError)
- Verify variable names in scoring prompt match function parameters
- Check the Traces UI → Inputs panel to see actual parameter names
- Escape JSON braces in prompts: use `{{` and `}}`

### max_tokens error
- Switch Judge model from `gpt-4o` to `gpt-4`
- This is a known compatibility issue

## Related Resources

- [Weave Monitor Documentation - Prompt Variables](https://docs.wandb.ai/weave/guides/evaluation/guardrails_and_monitors#prompt-variables)
- [Online Evaluation Guide](https://docs.wandb.ai/weave/guides/evaluation/guardrails_and_monitors)
- [Scorers Documentation](https://docs.wandb.ai/weave/guides/evaluation/scorers)

## License

MIT

## Contributing

This is a demonstration repository. For questions or issues with Weave itself, please contact [W&B Support](https://wandb.ai/support).
