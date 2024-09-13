# 定义输入字符串
input_data = """
586c0830-e2e3-0cda-48a3-d75b476ff82d
ca7b398d-a429-4347-79c5-9b51265ec387
7874bc77-573e-2f0b-e15c-c69d8caf2b07
02acf0d5-e73b-dc06-8d75-d0f5ad7a6d67
623657f5-6822-f7f1-696c-d00cd8034a20
846c3b83-197c-9cdf-f38d-a360ecc6a1f7
"""

# 分割字符串并为每个部分加上单引号和逗号
output_list = [f"'{uuid.strip()}'" for uuid in input_data.strip().split('\n')]

# 输出结果
output_string = ",\n".join(output_list)
print(output_string)