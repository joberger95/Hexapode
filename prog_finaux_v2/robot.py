import pypot.dynamixel
import numpy 
import calcul 

class robot():
    def __init__(self):
        #Creation des ports et du dxl_io
        #Analyse des ports et ouverture de la liaison série
        ports=pypot.dynamixel.get_available_ports()
        with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
            #scan du robot
            found_ids=dxl_io.scan()
            found_ids=found_ids[:-1]
            print(found_ids)
            print("DXL_IO= ",dxl_io)

        #Creation des tableaux de positions
        self.leg_init_pos[(160,0,90),
                        (160,0,90),
                        (160,0,90),
                        (160,0,90),
                        (160,0,90),
                        (160,0,90)]
        for i in [0,1,2,3,4,5,6]:
            print(self.leg_init_pos[i])
        self.leg_delta_pos[(0,0,0),
                        (0,0,0),
                        (0,0,0),
                        (0,0,0),
                        (0,0,0),
                        (0,0,0)] 

        def calculate_next_point(x,y,z):     
            for i in [0,1,2,3,4,5]:       
                self.leg_delta_pos[i]=self.leg_init_pos[i]+[( x , y , z )]
                print(self.leg_delta_pos[i])

        def set_goal_position():            
            dx=self.leg_delta_pos[0]
            dy=self.leg_delta_pos[1]
            dz=self.leg_delta_pos[2]
            for i in [1,2,3,4,5,6]:
                leg_id=i
                calcul.leg_move_delta(leg_id,dx,dy,dz)