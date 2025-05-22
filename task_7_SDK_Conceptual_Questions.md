# OpenAI Agents SDK: Core Concepts


## Why is the Agent class defined as a dataclass?

The Agent class is defined as a dataclass to simplify configuration by automatically generating methods like __init__ and __repr__. This reduces boilerplate code, aligns with the SDK's lightweight design, and ensures consistency with other data-holding classes, such as context.


## Why is the system prompt stored as instructions in the Agent class, and why can it be set as callable?

The system prompt, stored as instructions in the Agent class, defines the agent's behavior (e.g., "You are a helpful assistant"). It can be a static string for simplicity or a callable function to enable dynamic behavior based on specific scenarios, enhancing flexibility for complex workflows.


## Why is the user prompt passed as a parameter in the run method of Runner, and why is it a classmethod?

The user prompt is passed to the run method (e.g., Runner.run_sync) to provide runtime input, separate from the agent's configuration. As a classmethod, it allows direct invocation without creating a Runner instance, promoting ease of use and aligning with the SDK's simplicity.


## What is the purpose of the Runner class?

The Runner class serves as the entry point for executing agents, processing user prompts, and coordinating tool usage and LLM interactions. It provides methods like run_sync and run for synchronous or asynchronous execution, streamlining agent operations.


## What are generics in Python, and why are they used for TContext?

Generics in Python, enable classes to work with various data types while ensuring type safety. For TContext, generics allow the Agent class to handle different context types (e.g., UserContext), providing flexibility and type-safe access to context data in multi-agent workflows.
