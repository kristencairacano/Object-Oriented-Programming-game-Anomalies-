import time

questions = {1: "Where have you come from?",
             2: "Why should I let you in?",
             3: "Have you noticed anything unusual about yourself lately?",
             4: "Where were you when the first outbreak occurred?",
             5: "Is there anyone waiting for you inside?"}

#_____________________________________________________________
# Individual parent class
#_____________________________________________________________

class Individual:
    # All anomaly defenitions.
    ANOMALIES = {1: "Delayed Speech",
        2: "Unusual Pallor",
        3: "Irregular Breathing",
        4: "Irregular Tremors",
        5: "Speech Impediment",
        6: "Inappropriate Responses"}

    #initializing code for each subclass/objject
    def __init__(self,
        name,
        backstory,
        appearance,
        dialogues,
        anomaly_id=None):
        self.name = name
        self.backstory = backstory
        self.appearance = appearance
        self.dialogues = dialogues
        self.anomaly_id = anomaly_id

        self.asked_questions = set()
        self.is_inspected = False

#_____________________________________________________________
# Functions / Methods para sa individuals (Sila Ten n dito)
#_____________________________________________________________
def answer_question(self, question_id):
        if question_id not in self.dialogues:
            return "Invalid question."

        if question_id in self.asked_questions:
            return "You have already asked this question."

        self.asked_questions.add(question_id)
        response = self.dialogues[question_id]

        # DIALOGUE ANOMALIES
        if self.anomaly_id == 1:  # Delayed Speech
            sys.stdout.write("... They stare through the glass, hesitating ")
            for _ in range(3):
                time.sleep(0.7)
                sys.stdout.write(".")
                sys.stdout.flush()
            print("\n")

        elif self.anomaly_id == 2:  # Irregular Breathing
            words = response.split()
            if len(words) > 4:
                mid = random.randint(1, len(words) - 2)
                breath_sounds = ["... ahh ...", "... wheeze ...", "... gasp ...", "... hss ..."]
                words.insert(mid, random.choice(breath_sounds))
            response = " ".join(words)

        elif self.anomaly_id == 3:  # Verbal Tremors (Max is 3 tremors to avoid too many/it being unnatural.)
            words = response.split()
            valid = [i for i, w in enumerate(words) if len(w.strip(".,!?-")) > 3]
            if valid:
                for i in random.sample(valid, min(random.randint(1, 3), len(valid))): 
                    clean = words[i].strip(".,!?-")
                    words[i] = f"{clean[0]}-{words[i]}"
            response = " ".join(words)

        elif self.anomaly_id == 4:  # Speech Impediment (Max is 3 tremors to avoid too many/it being unnatural.)
            words = response.split()
            valid = [i for i, w in enumerate(words) if len(w.strip(".,!?-")) > 4]
            if valid:
                for i in random.sample(valid, min(random.randint(1, 3), len(valid))):
                    clean = words[i].strip(".,!?-")
                    chars = list(clean[1:-1])
                    random.shuffle(chars)
                    words[i] = words[i].replace(clean, clean[0] + "".join(chars) + clean[-1])
            response = " ".join(words)

        elif self.anomaly_id == 5:  # Inappropriate Responses
            other_keys = [k for k in self.dialogues.keys() if k != question_id]
            if other_keys:
                wrong_key = random.choice(other_keys)
                response = f"... {self.dialogues[wrong_key]}"

        elif self.anomaly_id == 6:  # Eerie Echo
            words = response.split()
            if words:
                last_word = words[-1].strip(".,!?-")
                response += f".. {last_word}..."

        elif self.anomaly_id == 7:  # Weird Slips
            weird_slips = [
                " It is surprisingly quiet inside my head.",
                " I... sorry, I lost my train of thought for a second.",
                " It's hard to remember what day of the week it is.",
                " Everything just... feels so quiet lately.",
                " I guess I'm... we're all just tired of walking.",
            ]
            response += random.choice(weird_slips)

        return response

    def inspect_appearance(self):
        self.is_inspected = True
        description = self.appearance

        # PHYSICAL ANOMALIES
        if self.anomaly_id == 3:  # Physical Tremors
            tremor_descriptions = [
                " Their knuckles look stiff and slightly rigid.",
                " Their fingers twitch with a faint tremor.",
                " They keep shifting their weight from one foot to the other.",
                " They adjust their collar twice in a row."
            ]
            description += random.choice(tremor_descriptions)

        elif self.anomaly_id == 8:  # Unusual Pallor
            pallor_descriptions = [
                " Their skin looks unusually pale.",
                " They look a bit washed out under the room's lighting.",
                " Their skin looks slightly dull, like someone who needs sleep.",
                " They have faint shadows under their eyes and pale cheeks."
            ]
            description += random.choice(pallor_descriptions)

        elif self.anomaly_id == 9:  # Infrequent Blinking
            blinking_descriptions = [
                " Their eyes stay wide and fixed on you the whole time.",
                " They don't seem to look away or glance around at all.",
                " Their eyelids barely move, even when you lean in closer."
            ]
            description += random.choice(blinking_descriptions)

        elif self.anomaly_id == 10:  # Faint Discoloration
            discoloration_descriptions = [
                " There's a tiny dark spot near the corner of their mouth.",
                " Their lower lip looks slightly dry and purple on one side.",
                " A faint mark sits near their bottom lip, almost like a smudge of purple."
            ]
            description += random.choice(discoloration_descriptions)

        elif self.anomaly_id == 11:  # Lag in Expression
            lag_descriptions = [
                " They blink once, then slowly nod a second later.",
                " Their mouth twitches slightly before they settle into a neutral look.",
                " Their expression settles a beat too late.",
                " Their head turns toward you first, followed by their gaze."
            ]
            description += random.choice(lag_descriptions)
        
        return description

    def get_anomaly_name(self):
        if self.anomaly_id is None:
            return "No anomaly"
        
        return self.ANOMALIES.get(self.anomaly_id, "Unknown anomaly")
    
#_____________________________________________________________
# Characters. Define each subclass of individual as each character
#_____________________________________________________________

class Pandemic_Survivor_1(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Pandemic Survivor 1",
            backstory="A doctor who tried and failed to find a cure.",
            appearance="A traveller who appears to have been travelling for years. They are wearing a worn-out backpack, and have dark circles under their eyes.",
            dialogues={1: "I come from the east, I've been moving from place to place since I left my home. I hope I can finally find a place to stay.",
                2: "I don't have a lot to offer, I just need a shelter to stay in.",
                3: "I've been feeling tired lately, but I guess that's normal when you've been walking for days.",
                4: " In my hometown, everybody was living so peacefully, it was a rather quiet place in the countryside, but everything just fell apart so quickly.",
                5: "Not that I know of, but hopefully I can find somebody I know in there"
            }, anomaly_id=anomaly_id)

class Walang_Pagkain_Buseng(Individual):
    pass

class Doctor(Individual):
    pass



# Test dito:
question = questions[1]
person = Pandemic_Survivor_1(anomaly_id=1)

print(question)
print("\nPandemic Survivor 1:")
print(person.answer_question(1))
print("\nAnomly type:")
print(person.get_anomaly_name())
