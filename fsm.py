class InterviewFSM:
    def __init__(self):
        self.state = "START"

    def start(self):
        print("\n--- Interview Process Started ---")
        self.state = "TECH"

    def technical_round(self):
        print("\n--- Technical Round ---")
        try:
            score = int(input("Enter candidate technical score (0-100): "))
            
            if score >= 50:
                print("Candidate passed technical round ✅")
                self.state = "FOLLOW_UP"
            else:
                print("Candidate failed technical round ❌")
                self.state = "END"
        
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    def follow_up_round(self):
        print("\n--- Follow-up Round ---")
        choice = input("Did candidate perform well? (yes/no): ").lower()
        
        if choice == "yes":
            print("Candidate selected ")
        else:
            print("Candidate rejected ")
        
        self.state = "END"

    def end(self):
        print("\n--- Interview Process Ended ---")

    def run(self):
        while True:
            if self.state == "START":
                self.start()

            elif self.state == "TECH":
                self.technical_round()

            elif self.state == "FOLLOW_UP":
                self.follow_up_round()

            elif self.state == "END":
                self.end()
                break


# Run the FSM
if __name__ == "__main__":
    fsm = InterviewFSM()
    fsm.run()
