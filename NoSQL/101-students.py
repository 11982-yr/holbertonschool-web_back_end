#!/usr/bin/env python3
"""returns students sorted by average score"""


def top_students(mongo_collection):
    """Return all students sorted by average score"""

    students = list(mongo_collection.find())

    for student in students:
        topics = student.get("topics", [])
        avg = sum(topic["score"] for topic in topics) / len(topics)
        student["averageScore"] = avg

    students.sort(key=lambda x: x["averageScore"], reverse=True)

    return students
