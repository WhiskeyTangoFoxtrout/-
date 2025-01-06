//I need away to figure when this run its also execute the windows(kern) app
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>

/*USE 4 SPACES NOT TABS AT ALL FOR CPYTHON*/
/*and remeber to K.I.S.S*/
/*I think this is a BootLoader Skeleton*/
int main(){

    static void BootJump(uint32_t *Address){

        if(CONTROL_1PRIV_Msk&__get_CONTROL()){

            EnablePrivilegedMode();/*Make sure Priv mode is set on so the reader can upload and read*/
        }
        NVIC->[0] = 0xFFFFFFFF;/*this clears interuptions*/
        NVIC->[1] = 0xFFFFFFFF;
        NVIC->[2] = 0xFFFFFFFF;
        NVIC->[3] = 0xFFFFFFFF;
        NVIC->[4] = 0xFFFFFFFF;
        NVIC->[5] = 0xFFFFFFFF;
        NVIC->[6] = 0xFFFFFFFF;
        NVIC->[7] = 0xFFFFFFFF;

        SysTick -> CTRL = 0;
        SCB -> ICSR |= SCB_ICSR_PENDDSTCLR_Msk;/*This is like a try and except method*/

        SCB->SHCSR &= ~( SCB_SHCSR_USGFAULTENA_Msk |\
        SCB_SHCSR_BUSFAULTENA_Msk |\
        SCB_SHCSR_MEMFAULTENA_Msk );
        /*I was being Lazy still going to steal code for the frame*/    

        if(CONTROL_SPSEL_Msk& __get_CONTROL())
        {/*it no greenlite*/

            __set_MSP(__get_PSP());
            __set_CONTROl(__get_CONTROL()& ~CONTROL_SPSPEL_Msk);
            
        }
        
        SCB->VTOR = (uint32_t)Address;
        BootJumpASM(Address[0],Address[1]);
    }

}
