import pretty_midi
import random

NOTES = [60, 62, 64, 65, 67, 69, 71, 72]


def generate_melody(length=16):
    melody = []

    for _ in range(length):
        note = random.choice(NOTES)
        duration = random.choice([0.25, 0.5, 1.0])

        melody.append((note, duration))

    return melody


def melody_to_midi(melody, output_file="output.mid"):
    midi = pretty_midi.PrettyMIDI()

    instrument = pretty_midi.Instrument(program=0)

    current_time = 0

    for pitch, duration in melody:
        note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=current_time,
            end=current_time + duration,
        )

        instrument.notes.append(note)

        current_time += duration

    midi.instruments.append(instrument)

    midi.write(output_file)

    return output_file


if __name__ == "__main__":
    melody = generate_melody()

    file = melody_to_midi(melody)

    print(f"Generated: {file}")
