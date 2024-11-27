vSmart1# show omp tlocs | tab
C   -> chosen
I   -> installed
Red -> redistributed
Rej -> rejected
L   -> looped
R   -> resolved
S   -> stale
Ext -> extranet
Stg -> staged
IA  -> On-demand inactive
Inv -> invalid

                                                                                                                                                PUBLIC           PRIVATE          
ADDRESS                                                                      PSEUDO                   PUBLIC                   PRIVATE  PUBLIC  IPV6    PRIVATE  IPV6     BFD     
FAMILY   TLOC IP          COLOR            ENCAP  FROM PEER        STATUS    KEY     PUBLIC IP        PORT    PRIVATE IP       PORT     IPV6    PORT    IPV6     PORT     STATUS  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ipv4     10.10.10.11      public-internet  ipsec  10.10.10.11      C,I,R     1       202.100.10.1     14360   10.1.10.1        12346    ::      0       ::       0        -       
         10.10.10.12      public-internet  ipsec  10.10.10.12      C,I,R     1       202.100.10.1     12346   202.100.10.1     12346    ::      0       ::       0        -       
         10.10.10.20      public-internet  ipsec  10.10.10.20      C,I,R     1       202.100.20.1     12346   202.100.20.1     12346    ::      0       ::       0        -       
         10.10.10.30      public-internet  ipsec  10.10.10.30      C,I,R     1       202.100.30.1     5103    10.1.3.3         12346    ::      0       ::       0        -       
         10.10.10.41      public-internet  ipsec  10.10.10.41      C,I,R     1       202.100.41.1     12346   202.100.41.1     12346    ::      0       ::       0        -       
         10.10.10.42      public-internet  ipsec  10.10.10.42      C,I,R     1       202.100.42.1     12346   202.100.42.1     12346    ::      0       ::       0        -       
         10.10.10.50      public-internet  ipsec  10.10.10.50      C,I,R     1       202.100.50.1     12346   202.100.50.1     12346    ::      0       ::       0        -       