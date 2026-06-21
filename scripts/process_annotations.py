import pandas as pd

input_file = "../video_4.csv"
df = pd.read_csv(input_file)

def update_annotation(row):
    tier = row['Tier']
    annotation = row['Annotation']

    if annotation == "Yes":
        return tier
    elif annotation == "Fork_towards":
        return "Fork_towards_left" if "left" in tier.lower() else "Fork_towards_right"
    elif annotation == "Look_at_plate":
        return "Look_at_plate_left" if "left" in tier.lower() else "Look_at_plate_right"
    elif annotation == "Look_towards":
        return "Look_at_plate_left" if "left" in tier.lower() else "Look_at_plate_right"
    else:
        return annotation

df['Annotation'] = df.apply(update_annotation, axis=1)
df.drop('Tier', axis=1, inplace=True)

output_file = "updated_file.csv"
df.to_csv(output_file, index=False)

print(f"File has been processed and saved as {output_file}")
