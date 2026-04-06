stories = {1:"allien.txt",2:"fantasy.txt",3:"school.txt"}

print("Available stories:")
for num,filename in stories.items():
    print(f"{num} : {filename}")

choice = int(input("Enter the num of the story you want to fill:"))
if choice in stories:
    print(f"you choose story {choice}:{stories[choice]}")
    with open(stories[choice],"r") as f:
        story_text = f.read()
else:
  print("choose a valid option")

words = set()
start_of_word = -1
target_start ="<"
target_end = ">"

for i,char in enumerate(story_text):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story_text[start_of_word: i+1]
        words.add(word)
        start_of_word = -1


answers = {}

for word in words:
    answer = input("Emter the word for" + word + ":")
    answers[word] = answer

for word in words:
   story_text = story_text.replace(word, answers[word])

print(story_text)


