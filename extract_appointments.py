from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

from schemas import Appointment

client = Anthropic()

SYSTEM = """You read messages sent to a clinic and fill in an appointment form.

Rules:
- TODO: Only extract information that is clearly in the message.
If something is missing or unclear, use null. Never guess names, dates,
times, or numbers.

- TODO: Respond with valid JSON only. No explanations, no markdown.
Use exactly this format:
{
  "Name": string | null,
  "Phone": string | null,
  "Doctor": string | null,
  "date": "YYYY-MM-DD" | null,
  "time": "HH:MM" | null,
  "clean_message": string,
  "needs_human_review": boolean,
  "urgent": boolean
}.

- TODO: Never diagnose, give treatment advice, or answer medical questions.
If the message is unclear, mentions pain, emergency, or symptoms,
set needs_human_review to true so a staff member handles it.

- TODO: If the massage is not in English, translate it to English.

"""

MESSAGES = [
    "Assalam o Alaikum, I'm Ayesha Khan. I need to see a dentist on Monday morning because my tooth hurts. My number is 0300-1234567.",
    "Bilal here. Eye checkup please, any day next week, in the evening.",
    "URGENT!! My son has had a high fever since last night. Can a doctor see him this afternoon? Call me on 0321-7654321. Sana",
    "hi i have a rash on my arm, want skin doctor on saturday. hamza 0333 5551234",
    "Can I book something for Friday?",
    "hey im usman i wanna see a doctor on monday, can you do it for me? i have a headache",
    "asalam o alikum, mera name usman hy, meri tabiyat kharab hai, mujhe doctor ki zarurat hai. mera number 0345-9876543",
    # TODO: add 2 messages of your own. One of them must be missing some information.
]

for number, message in enumerate(MESSAGES, start=1):
    # TODO: send `message` to Claude, with your SYSTEM rules and the Appointment form.
    # Hint: copy the client.messages.parse(...) call from day2/05_structured_claude.py
    appointment = None

    if appointment is None:
        print("Not finished yet: complete the TODO inside the loop.")
        break

    print(f"Message {number}: {message}")
    print(appointment.model_dump_json(indent=2))
    print()
