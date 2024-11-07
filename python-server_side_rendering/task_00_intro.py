#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Create the personalized invitation text by replacing placeholders
        invitation_text = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Replace each placeholder with actual value or "N/A" if missing
            value = attendee.get(key, "N/A") or "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", value)

        # Write the personalized invitation to a file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation_text)
            print(f"Invitation file created: {output_filename}")
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")
