//imports

#include <pcap.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <pcap.h>


/* default snap length (maximum bytes per packet to capture) */
#define SNAP_LEN 1024

/* ethernet headers are always exactly 14 bytes [1] */
#define SIZE_ETHERNET 14

/* Ethernet addresses are 6 bytes */
#define ETHER_ADDR_LEN 6



/* Ethernet header */
struct sniff_ethernet {
  u_char  ether_dhost[ETHER_ADDR_LEN];    /* destination host address */
  u_char  ether_shost[ETHER_ADDR_LEN];    /* source host address */
  u_short ether_type;                     /* IP? ARP? RARP? etc */
};

/* IP header */
struct sniff_ip {
  u_char  ip_vhl;                 /* version << 4 | header length >> 2 */
  u_char  ip_tos;                 /* type of service */
  u_short ip_len;                 /* total length */
  u_short ip_id;                  /* identification */
  u_short ip_off;                 /* fragment offset field */
  u_char  ip_ttl;                 /* time to live */
  u_char  ip_p;                   /* protocol */
  u_short ip_sum;                 /* checksum */
  struct  in_addr ip_src,ip_dst;  /* source and dest address */
};


#define IP_HL(ip)               (((ip)->ip_vhl) & 0x0f)
#define IP_V(ip)                (((ip)->ip_vhl) >> 4)

/* TCP header */
typedef u_int tcp_seq;

struct sniff_tcp {
  u_short th_sport;               /* source port */
  u_short th_dport;               /* destination port */
  tcp_seq th_seq;                 /* sequence number */
  tcp_seq th_ack;                 /* acknowledgement number */
  u_char  th_offx2;               /* data offset, rsvd */

#define TH_OFF(th)      (((th)->th_offx2 & 0xf0) >> 4)
  u_short th_win;                 /* window */
  u_short th_sum;                 /* checksum */
  u_short th_urp;                 /* urgent pointer */
};

/* determine protocol */
/* void determine_protocol(struct ip) { */
/*   switch(ip->ip p) { */
/*   case IPPROTO TCP: */
/* 	printf("   Protocol: TCP\n"); */
/* 	break; */
/*   case IPPROTO UDP: */
/* 	printf("   Protocol: UDP\n"); */
/* 	return; */
/*   case IPPROTO ICMP: */
/* 	printf("   Protocol: ICMP\n"); */
/* 	return; */
/*   case IPPROTO IP: */
/* 	printf("   Protocol: IP\n"); */
/* 	return; */
/*   default: */
/* 	printf("   Protocol: unknown\n"); */
/* 	return; */
/*   } */
/* } */

int main(int argc, char *argv[])
{
  char *dev, errbuf[PCAP_ERRBUF_SIZE];

  dev = pcap_lookupdev(errbuf);
  if (dev == NULL) {
	fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
	return(2);
  }
  printf("Device: %s\n", dev);
  return(0);
}
