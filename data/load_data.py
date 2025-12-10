from datasets import load_from_disk

# from datasets import load_dataset
# dataset = load_dataset("hotpotqa/hotpot_qa", "distractor")

dataset = load_from_disk("./hotpot_qa_raw")

print(dataset)


sample = dataset['train'][0]
print("Câu hỏi:", sample['question'])
print("Câu trả lời:", sample['answer'])
print("Context (Document):", sample['context']['sentences'][0])

# dataset.save_to_disk("./hotpot_qa_raw")