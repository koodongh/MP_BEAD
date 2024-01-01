from pylogix import PLC
import time
import _H2104_detect
def PLC_():
    with PLC() as comm:
        comm.IPAddress = '100.100.100.1'  # PLC의 IP 주소

        # bool 태그 정의
        tag_trigger = 'BP_Camera_Trigger'  # 예시: 카메라 트리거
        tag_OK = 'BP_Camera_OK'            # 예시: OK 신호
        tag_NG = 'BP_Camera_NG'            # 예시: NG 신호
        tag_Ready = 'BP_Camera_Ready'      # 예시: 준비 상태
        tag_Height = 'BP_Camera_Packing_Height'  # 실수 태그
        tag_Spec = 'BP_Camera_Spec'        # 실수 태그
        tag_TEST = 'BP_Camera_Test'
        # Camera On
        comm.Write(tag_TEST, True)
        
        # Trigger On 
        is_trigger = comm.Read(tag_trigger).Value
        if is_trigger == True :
        # bool 태그에 데이터 쓰기
            comm.Write(tag_trigger, False)  # 예시: 카메라 트리거를 활성화
            comm.Write(tag_OK, False)   # 예시: 준비 상태를 비활성화
            comm.Write(tag_NG, False)   # 예시: 준비 상태를 비활성화
            comm.Write(tag_Ready, True)   # 예시: 준비 상태를 비활성화
            # bool 태그에서 데이터 읽기
            is_Spec = comm.Read(tag_Spec).value
            is_Height = comm.Read(tag_Height).value
            if is_Spec != 0 :
                # 카메라 촬영하는 코드
                #main.cam()
                # 이미지 모델 실행 코드
                #if is_Height != 0:
                    #Result = _H2104_detect.main(is_Height)
                # test
                comm.Write(tag_TEST,True)
                time.sleep(3)
                print('----AI Detect----')
                Result = 0
                if Result == 0 :
                    comm.Write(tag_OK, True)
                else: 
                    comm.Write(tag_NG, True)
                
                if Result == 0:
                    print(f'Successfully wrote {Result} to {tag_Spec}')
                else:
                    print(f'Failed to write to {tag_Spec}')

                # 결과 출력
                is_OK = comm.Read(tag_OK)
                is_NG = comm.Read(tag_NG)

                #comm.Write(tag_Ready, False)
                is_Cam = comm.Read(tag_Ready)
                is_Test = comm.Read(tag_TEST)

                print(f"OK Status: {is_OK.Value}")
                print(f"NG Status: {is_NG.Value}")
                print(f"Cam Status: {is_Cam.Value}")
                print(f"Test Status: {is_Test.Value}")
        

if __name__ == '__main__':
    while True:
        PLC_()
        print('----Wait----')
        time.sleep(0.5)
