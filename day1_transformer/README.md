# Transformer Day 1 Exercise

# What is Generative AI?

Generative AI refers to a class of artificial intelligence systems designed to generate new content such as text, images, audio, or code based on patterns learned from large datasets. Instead of only making predictions or classifications, generative models learn the underlying distribution of data and can produce new outputs that resemble the training data.

Traditional machine learning systems are typically discriminative. They learn relationships between inputs and outputs and are commonly used for tasks such as classification or regression. For example, a traditional machine learning model might predict whether an email is spam or not.

Generative AI models, on the other hand, learn how data is structured and can create entirely new examples. Modern Generative AI systems are commonly built using Transformer architectures and large language models (LLMs).

Some well-known examples include models capable of generating human-like text, synthesizing images from prompts, or producing code from natural language instructions.

### Real-world Applications

1. **Conversational AI** – Intelligent assistants and chatbots capable of natural language conversations.
2. **Content Generation** – Automatic writing of articles, marketing copy, or programming code.
3. **Image Generation** – Creating realistic images from text prompts.

Generative AI is now a core technology powering many modern AI products and research advancements.

---

# Self-Attention Explained (Example)

Consider the sentence:

"The cat sat on the mat"

Self-attention allows each word in the sentence to understand its relationship with other words.

For every word, three vectors are created:

| Component | Purpose |
|-----------|--------|
| Query (Q) | Represents what the word is looking for |
| Key (K) | Represents what the word offers |
| Value (V) | Contains the actual information associated with the word |

For example, when processing the word **"sat"**, the model compares its Query vector with the Key vectors of all other words. This comparison determines which words are most relevant for understanding the meaning of "sat".

### Why do we scale by √d_k?

The dot product between Query and Key vectors can grow large when the vector dimension increases. Large values can push the softmax function into regions where gradients become very small, making training unstable. Dividing by √d_k stabilizes the values and improves training behavior.

### Why do we apply Softmax?

Softmax converts attention scores into probabilities that sum to one. This allows the model to determine how much importance should be assigned to each word when computing the final representation.

### What problem does attention solve?

Earlier sequence models such as RNNs processed text sequentially and struggled to capture long-range dependencies in sentences. Information from earlier tokens could fade as sequences grew longer.

Self-attention solves this by allowing every word to directly attend to every other word in the sentence. This enables the model to capture global context efficiently and allows parallel computation, significantly improving training speed and scalability.

---

# Encoder vs Decoder Comparison

| Component | Encoder | Decoder |
|-----------|--------|--------|
| Self Attention | Each token attends to all tokens in the input sequence | Uses masked self-attention to prevent future tokens from being visible |
| Masked Attention | Not used | Ensures the model predicts tokens autoregressively |
| Cross Attention | Not present | Allows the decoder to attend to encoder outputs |
| Primary Role | Encode input sequence into contextual representations | Generate output sequence step by step |

**Masked Attention:** Prevents the decoder from seeing future tokens during training.

**Cross-Attention:** Enables the decoder to reference encoder outputs when generating predictions.

Encoders are typically used for understanding input data, while decoders are responsible for generating outputs.

---

# Vision Transformers (ViT)

Vision Transformers apply the Transformer architecture to image processing tasks. Instead of processing images using convolutional filters like CNNs, Vision Transformers treat images as sequences of patches.

An image is first divided into small fixed-size patches, typically 16×16 pixels. Each patch is flattened into a vector and projected into an embedding space, similar to how words are embedded in natural language processing tasks. These patch embeddings become tokens that are fed into the Transformer.

Because Transformers do not inherently understand spatial structure, positional embeddings are added to each patch token. These embeddings encode the position of each patch within the image, allowing the model to understand spatial relationships.

Conceptually, this approach differs from convolutional neural networks. CNNs rely on convolutional kernels that exploit local spatial patterns and translation invariance. Vision Transformers instead rely entirely on self-attention mechanisms to learn relationships between image regions.

This allows the model to capture global dependencies across the entire image rather than focusing only on local neighborhoods. While CNNs remain highly effective for many vision tasks, Vision Transformers have demonstrated strong performance on large-scale datasets and are now widely used in modern computer vision research.