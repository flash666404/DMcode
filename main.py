import re

SVO = "SVO"
SOV = "SOV"
VSO = "VSO"
VOS = "VOS"
UNKNOWN = "OTHER"
SVO1 = "SVO1"
SOV1 = "SOV1"
VSO1 = "VSO1"
VOS1 = "VOS1"

# Proportion of statistical language order
def count_syntax(file_path):
    total = 0
    svo_count = 0
    sov_count = 0
    vso_count = 0
    vos_count = 0
    unknown_count = 0

    with open(file_path, "r") as f:
        contents = f.read()

    # Matching sentences with regular expressions
    pattern = re.compile(r"[A-Z][^\.!?]*[\.!?]")
    sentences = pattern.findall(contents)

    # Traversing sentences and counting order
    for sentence in sentences:
        total += 1
        words = sentence.split()
        if len(words) < 3:
            unknown_count += 1
            continue
        if words[1] == "is" or words[1] == "am" or words[1] == "are":
            svo_count += 1
        elif words[0] == "It" and words[2] == "is":
            svo_count += 1
        elif words[1] == "has" or words[1] == "have":
            svo_count += 1
        elif words[0].endswith("ly") or words[0].endswith("ing"):
            vso_count += 1
        elif words[1] == "am" or words[1] == "is" or words[1] == "are":
            svo_count += 1
        elif words[0].lower() == "there":
            svo_count += 1
        elif words[0] == "Let" and words[1] == "us":
            svo_count += 1
        elif words[0] == "You" and words[1] == "are":
            svo_count += 1
        elif words[1] == "must":
            svo_count += 1
        elif words[0].lower() == "if":
            svo_count += 1
        elif words[0].lower() == "although":
            svo_count += 1
        elif words[-2] == "to":
            vos_count += 1
        else:
            unknown_count += 1


    svo_ratio = float(svo_count) / total
    sov_ratio = float(sov_count) / total
    vso_ratio = float(vso_count) / total
    vos_ratio = float(vos_count) / total
    unknown_ratio = float(unknown_count) / total

    sum1 = float(svo_count)+ float(sov_count) + float(vso_count)+ float(vos_count)
    svo_ratio1 = float(svo_count) / sum1
    sov_ratio1 = float(sov_count) / sum1
    vso_ratio1 = float(vso_count) / sum1
    vos_ratio1 = float(vos_count) / sum1

    return {
        SVO: svo_ratio,
        SOV: sov_ratio,
        VSO: vso_ratio,
        VOS: vos_ratio,
        UNKNOWN: unknown_ratio,

        SVO1: svo_ratio1,
        SOV1: sov_ratio1,
        VSO1: vso_ratio1,
        VOS1: vos_ratio1,
    }


result = count_syntax("all.txt")
print(result)
