from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '100.100.100.1'  # PLC의 IP 주소로 변경하세요
    #tag = 'HMI_BEAD_PACKING_HALF_HEIGHT'  # 읽고 싶은 태그 이름으로 변경하세요
    tag = 'HMI_BEAD_PACKING_SPEC'  # 읽고 싶은 태그 이름으로 변경하세요

    ret = comm.Read(tag)
    #string_value = comm.ReadString(ret)
    #bit_number = 0  # 읽고 싶은 비트 번호
    #bool_value = comm.Read(f'{ret}.{bit_number}')
    # bit
    #data_length = 10  # 읽고 싶은 데이터의 길이 (바이트 단위)
    #response = comm.Read(tag, data_length)
        
    if ret.Status == 'Success':
        print(f'Tag Value: {ret.Value}')
        # string
        #print(f'String Value: {string_value.Value}')
        # bool
        #print(f'Bool Value: {bool_value.Value}')
        # bit
        #byte_array = response.Value  # 바이트 배열
        #print("Read Bytes:", byte_array)
    else:
        print(f'Error: {ret.Status}')


'''
# 보내는 코드

float_tag = 'YourFloatTag'  # 부동소수점 태그 이름으로 변경하세요
float_value = 123.45  # 쓰고 싶은 부동소수점 값

status = comm.Write(float_tag, float_value)
if status:
    print(f'Successfully wrote {float_value} to {float_tag}')
else:
    print(f'Failed to write to {float_tag}')


'''