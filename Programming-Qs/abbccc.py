# Input: "aazzzzbbvvvvvvbbbbbbccc"
# Output: "a2z4b8v6c3"

def convert_string(input_str):
  freq = {}
  for char in input_str:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  output_str = ""
  for key, value in freq.items():
    output_str += key + str(value)
    
  return output_str

input_str = "aazzzzbbvvvvvvbbbbbbccc"
print(convert_string(input_str))