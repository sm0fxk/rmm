


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


enum request_type {get_request, set_request};

#define BUFFER_SIZE 80
char commandbuffer[BUFFER_SIZE];

typedef struct cmd_entry
{
    char cmd[3];
    void (*fun)(char*);
} cmd_entry;

static void  radio_model(char*);
static void  modem_config(char*);
static void  transmit_power(char*);
static void  trcv_register(char*);
static void  set_frequency(char*);
static void  read_rssi(char*);
static void  trcv_status(char*);
static void  error(char*);



cmd_entry cmd_table[] = {

                         {"ID", radio_model},
                         {"MD", modem_config},  
                         {"PC", transmit_power},      
                         {"RE", trcv_register},
                         {"FA", set_frequency},
                         {"SM", read_rssi},
                         {"IF", trcv_status},
                         {"",   error} };
                         
                         
enum request_type request(char *param)
{
  if(strlen(param) == 0)
     return(get_request);
  else
     return(set_request);
}
                       
void radio_model(char* args)
{
	fputs("CC110x\n", stdout);
}

void modem_config(char* args)
{
	printf("['GFSK, Data Rate: 1.2kBaud, Dev: 5.2kHz, RX BW 58kHz',");
	printf("'GFSK, Data Rate: 2.4kBaud, Dev: 5.2kHz, RX BW 58kHz']\n");
}
void transmit_power(char* args)
{  
	switch (request(args))
    {
      case get_request:
         printf("['-30', '-20', '-15', '-10', '0', '5', '7','10']\n");
         break;
      
      
      case set_request:
         printf("set\n");
         break;      
  }
}
void trcv_register(char* args)
{
	switch (request(args))
    {
      case get_request:
         printf("01,62\n");
         break;
      
      
      default:
         printf("1A\n");
         break;      
  }
}
void set_frequency(char* args)
{
}
void read_rssi(char* args)
{
}
void trcv_status(char* args)
{
}
void error(char* args)
{
}                    
                         
//======================================================================
//
//======================================================================
int get_line(){
  int pos = 0;

  while(1) {
    if(pos < BUFFER_SIZE){
      int ch = getchar();
      if(ch == '\n' || ch ==0 || ch == -1) {
//        commandbuffer[pos++] = ch;
        commandbuffer[pos] = 0;
//        Serial.println("End of buffer found");
        return(0);
      }
      else{
//        Serial.println("Adding ch");
        commandbuffer[pos++] = ch;
      };
    }
    else {
//      Serial.println("Buffer overflow");
      commandbuffer[pos] = 0;
      return(1); 
    };
  };
}

void parse_command(int status)
{
  int i=0;
//  Serial.print("String to be parsed: ");
//  Serial.println(commandbuffer);
  for(i = 0; strncmp(commandbuffer, cmd_table[i].cmd, 2) && strcmp(cmd_table[i].cmd, ""); i++);
    (*cmd_table[i].fun)(&commandbuffer[2]);
   
}  
   
   
    
int main()
{
    setbuf(stdout, NULL); // make it unbuffered
        
    size_t size;
    while(1)
    {
    get_line();
    parse_command(0);
    
    
//    printf("%s", commandbuffer);
    }
 /*  
    char *line = buffer;
    if (getline(&line, &size, stdin) == -1) {
        printf("No line\n");
    } else {
        printf("%s\n", line);
    }
    return 0;
    
 */   
    
    
    
 /*     
        size_t  n = 80;
        char * p =buffer;
        getline(&p, &n, stdin);
        
        fprintf(stderr, "%s\n", "msg received");

        printf("%s\n", "Hello!");
        
*/
/*
        while(1)
        {
           get_line();
           if(strlen(commandbuffer) > 1)
           {
          // fprintf(stderr, "%s %s\n", "msg received", buffer);
           printf("%s", commandbuffer);
           
           
           if( strncmp(commandbuffer, "EX", 2) == 0)
               exit(0);
           if(strncmp(commandbuffer, "QR", 2) == 0) 
               fputs("CC110x\n", stdout);
         }
               
	    }
*/	    
	    
}
