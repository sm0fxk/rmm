




#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>
enum request_type {get_request, set_request};

#define BUFFER_SIZE 80
char commandbuffer[BUFFER_SIZE];

typedef struct cmd_entry
{
    char cmd[3];
    void (*fun)(char*, char*);
} cmd_entry;

static void  radio_model(char*, char*);
static void  modem_config(char*, char*);
static void  transmit_power(char*, char*);
static void  trcv_register(char*,char*);
static void  frequency(char*,char*);
static void  read_rssi(char*,char*);
static void  trcv_status(char*,char*);
static void  error(char*, char*);

void get_radio_model(char* );
void get_modem_config(char* );
int get_trcv_register(int);
int set_trcv_register(int,int);
void get_transmit_power();
void init();
int set_frequency(unsigned long int);
int get_trcv_status();
int set_trcv_status(char* );
void get_trcv_register_range();

cmd_entry cmd_table[] = {

                         {"ID", radio_model},
                         {"MD", modem_config},  
                         {"PC", transmit_power},      
                         {"RE", trcv_register},
                         {"FA", frequency},
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
                       
void radio_model(char* args, char* reply)
{

	get_radio_model(reply);
}

void modem_config(char* args, char* reply)
{
	get_modem_config(reply);
}
void transmit_power(char* args, char* reply)
{  
	switch (request(args))
    {
      case get_request:
         get_transmit_power(reply);
         break;
      
      
      case set_request:
         printf("set\n");
         break;      
  }
}
void trcv_register(char* args, char* replybuffer)
{
    char *saveptr;
    char reg_addr[10];
    char value[10];
    int reply;
    char        *end;  

    switch (request(args))
    {
      case get_request:
         get_trcv_register_range(replybuffer);
         break;
      
      
      default:
         if(strchr(args, ',') == NULL)
         {
             reply = get_trcv_register(strtoul(args, &end, 10));
             sprintf(replybuffer, "%02x\n", reply);
         }
         else
         {
             strcpy(reg_addr, strtok_r(args, ",", &saveptr));
             strcpy(value, strtok_r(NULL, ",", &saveptr));
             reply = set_trcv_register(strtoul(reg_addr, &end, 10), strtoul(value, &end, 10));
             sprintf(replybuffer, "%d\n", reply);
	     }

//         fprintf(stderr, "%s", args);
         break;      
  }
}
void frequency(char* args, char* reply)
{
	unsigned long int freq;
    char        *end;  
	
	freq =  strtoul(args, &end, 10);
	set_frequency(freq);
//	fprintf(stderr, "%ld\n", freq);
	sprintf(reply, "OK\n");
	}
void read_rssi(char* args, char* reply)
{
}
void trcv_status(char* args, char* reply)
{
	switch (request(args))
    {
      case get_request:
         get_trcv_status();
         break;
      
      
      case set_request:
         set_trcv_status(args);
         break;      
  }
}
void error(char* args, char* reply)
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

void parse_command(char* commandbuffer, char* replybuffer)
{
  int i=0;
//  Serial.print("String to be parsed: ");
//  Serial.println(commandbuffer);
  for(i = 0; strncmp(commandbuffer, cmd_table[i].cmd, 2) && strcmp(cmd_table[i].cmd, ""); i++);
    (*cmd_table[i].fun)(&commandbuffer[2], replybuffer);
   
}  
   
   
    
int main()
{
   int sockfd, newsockfd, portno, clilen;
   char buffer[256];
   char reply_buffer[256];
   struct sockaddr_in serv_addr, cli_addr;
   int  n;
   


   init();
   /* First call to socket() function */
   sockfd = socket(AF_INET, SOCK_STREAM, 0);
   
   if (sockfd < 0) {
      perror("ERROR opening socket");
      exit(1);
   }
   
   /* Initialize socket structure */
   bzero((char *) &serv_addr, sizeof(serv_addr));
   portno = 5000;
   
   serv_addr.sin_family = AF_INET;
   serv_addr.sin_addr.s_addr = INADDR_ANY;
   serv_addr.sin_port = htons(portno);
   
   /* Now bind the host address using bind() call.*/
   if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
      perror("ERROR on binding");
      exit(1);
   }
      
   /* Now start listening for the clients, here process will
      * go in sleep mode and will wait for the incoming connection
   */
   
   listen(sockfd,5);
   clilen = sizeof(cli_addr);
   
   /* Accept actual connection from the client */
   newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
	
   if (newsockfd < 0) {
      perror("ERROR on accept");
      exit(1);
   }
   
   /* If connection is established then start communicating */
   while(1)
   {
      bzero(buffer,256);
      n = read( newsockfd,buffer,255 );
   
      if (n < 0) {
         perror("ERROR reading from socket");
         exit(1);
      }
   
//      printf("Here is the message: %s\n",buffer);
      parse_command(buffer, reply_buffer);
      /* Write a response to the client */
//      sprintf(reply_buffer, "%s\n", "(0,62)");
      n = write(newsockfd,reply_buffer,strlen(reply_buffer));

      if (n < 0) {
         perror("ERROR writing to socket");
         exit(1);
      }
   }  
   return 0;



/*
    init();
    while(1)
    {
    get_line();
    parse_command(0);
    
*/  

    
   
	    
}
