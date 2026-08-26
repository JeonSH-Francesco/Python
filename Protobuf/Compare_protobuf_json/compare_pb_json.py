import json
import user_pb2 as user_pb2

# ----------------------------------------------------------------------
# 1. Protobuf 직렬화
# ----------------------------------------------------------------------
user = user_pb2.User()
user.id = 1
user.name = "홍길동"
user.tags.append("developer")

pb_data = user.SerializeToString()
print("Protobuf 바이트열:", pb_data)
print(f"Protobuf 크기: {len(pb_data)} bytes")

# 역직렬화 확인
new_user = user_pb2.User()
new_user.ParseFromString(pb_data)
print("역직렬화 결과:", new_user.name)

print()

# ----------------------------------------------------------------------
# 2. JSON 직렬화 (같은 데이터)
# ----------------------------------------------------------------------
json_obj = {"id": 1, "name": "홍길동", "tags": ["developer"]}
json_data = json.dumps(json_obj, ensure_ascii=False).encode("utf-8")
print("JSON 문자열:", json_data)
print(f"JSON 크기: {len(json_data)} bytes")

print()
print(f"=== 크기 비교: JSON이 Protobuf보다 {len(json_data) / len(pb_data):.2f}배 큼 ===")

'''
python -m grpc_tools.protoc -I. --python_out=. user.proto 수행
'''
