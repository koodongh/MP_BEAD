from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '100.100.100.1'  # PLC의 IP 주소로 변경하세요
    #tag = 'HMI_BEAD_PACKING_HALF_HEIGHT'  # 읽고 싶은 태그 이름으로 변경하세요
    #tag = 'HMI_BEAD_PACKING_SPEC'  # 읽고 싶은 태그 이름으로 변경하세요
    #trigger_tag = 'BP_Camera_Trigger' bool
    #trigger-> Trigger/OK/NG
    #trigger_tag = 'BP_Camera_OK' bool
    #trigger_tag = 'BP_Camera_NG' bool
    #trigger_tag = 'BP_Camera_Ready' bool -> Yellow light

    #trigger_tag = 'BP_Camera_Packing_Height' real

    float_tag = 'HMI_BEAD_PACKING_SPEC'  # 부동소수점 태그 이름으로 변경하세요
    float_value = 1  # 쓰고 싶은 부동소수점 값

    status = comm.Write(float_tag, float_value)
    if status:
        print(f'Successfully wrote {float_value} to {float_tag}')
    else:
        print(f'Failed to write to {float_tag}')


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