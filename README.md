SIR
===

Skype Ip Resolver

![Screenshot](https://raw.githubusercontent.com/AeonDave/sir/master/doc/screenshot/sir.png)

## Description

SIR, is a simple tool which resolve from the net the last known ip of a Skype Name

## Download and install

You can download the latest version by cloning SIR from the Git repository:

	git clone https://github.com/AeonDave/sir.git
	
## Dependencies

For http data retrival i used BeautyfulSoup library so you need to install it into your python libraries. Don't worry, it's easy!

	pip install beautifulsoup4

or

	easy_install BeautifulSoup4
	
or you just simply download the library and then

	cd BeautifulSoup
	python setup.py install
	
## Thanks to:

BeautyfulSoup http://www.crummy.com/software/BeautifulSoup/
ResolveThem http://www.resolvethem.com/
	
	
	
	                                   .:rA@##@2                                                                
	                               .;h@@@@@@@@@@                                                                
	                          ;S@@@@@@@@@@@@@@@@@;                                                              
	                      :2M@@@@@@@@@@@@@@@@@@@@@A                                                             
	                  ;A@@@@@@@@@@@@@@@@@@@@@@@@@@@5                                                            
	              r&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                                                           
	           .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                           
	        .s#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2                                                          
	     .s@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                          
	   ,A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5                                                         
	  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@r                                                        
	   i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5                                                       
	     A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;                                                      
	      s@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                        .:                           
	        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                ,:X#@@@@@:                          
	        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;          ,S#@@@@@@@@@@@,                          
	         .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Mh5rrB:     r2@@@@@@@@@@@@@@M2                           
	           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@AXr,  .rG@@;S#M@@@@@@@@@@@@Hi:                               
	           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@A2;. .,r&@@@@@@@@@@@@@@@@@@9S.                                   
	            r@@@@@@@@@@@@@@@@@@@@@@@@@@A2;. .:5B@@@@@@@@@@@@@@@@#G;.                                        
	             i@@@@@@@@@@@@@@@@@@@@@hs:. .:sH@@@@@@@@@@@@@@@#ir                                              
	              ;@@@@@@@@@@@@@@@H2;,. ,;5&@@@@@@@@@@@@@#MH&B@#h:                                              
	               .@@@@@@@@@@Ahs.  ,s5H@@@@@@@@@@@@@@MAX2i;,..,;XAGX;,                                         
	                 @@@@#&2;.  .rA@@@@@@@@@@@@#AAAhs:,.            S@@@;                                       
	                  B;.  .:SA@@@@@@@@@@@#HHGXX5r.                    s@@,                                     
	                   Si9#@@@@@@@@@@@#B925S5i:    ;@@,              ..  A@,                                    
	                ;5@@@@@@@@@@@@AGX52XXS:.       ,@@@ASiis52XXX2XG##r   h@.                                   
	           ;h#@@@@@@@@@@@MBASi52Xi;,    .@,      G@@@@@@@@MM#MH@@5     @M                                   
	      .sA@@@@@@@@@@@@@H3Sri22i;          @@        :AM#    r3AGXM@&    ,@                                   
	   ;X@@@@@@@@@@@@@5.AMis5G9;     5MB@MMA@@@         :@  r2r. i@G @#     @A                                  
	;@@@@@@@@@@@@@hi,  ;@A293.    :#M525. .,2@@,        ,@ri.     .  @:     s@r       ,#@,                      
	;@@@@@@@@Mrir      @@2XX     G@, :r,    : M@,        @@         Mh       @#       ;@@@                      
	 i@@@@9,          3@9XS     G@  ;i:    r ,.,@;       ,@@5,   ,@@3 ,3@@@@M@@;        H@                      
	  SX.            ;@MSA. .rr&@  ;ir  . S,,;  5@         .SG@#M@3 ,#@@@@@@@@@@@@#SisX@@#                      
	                 A@ShS  .HG@B :5r  . s:,r   2@         ;:;s2i  s@@@@@2;   @@@@@@@@@@:           ;@2X333393#;
	                 B@SB:  H@#@A ss  . rr.S   ;r@      s@@@@@@@@@ @@@@H      &i  ;;:               M@        :G
	                 @@2X  @5;5@@rr. . ;r.S   r.;@    5@@@@@@@@@@@@3@@@,      2B                    9@         A
	                 #@9i  2:   @@.   :i.s   r,.@:   #@@@@H.  .#@@@  .. GS    @#                    X@         A
	                 #@hi   &    A@: ,s i.  :;;@,   A@@@M               3@;  .@2                    2@      .  A
	                 @@A5   #2    ;@@#:i.  s@#X     @@@2    GX   ;2Hh9;  @#  2@,                    ,@H3&&&@@@AM
	                 @@H5   Ar      ,2M#GBHAs      i@@h    X@i h@r;22;   ;A  M@                      @@@@@@@@B@A
	                 @#AS   @9               ,A@: .@@B     M@@  ,A#2:        @H                       r@@HAH#@G.
	                 #@AS   ;A               @H@9,@@@.      r@3  ,          ;@i                        :##@M9r  
	                 H@GG    @.              i@#@@@2                        H@                          i@X     
	                 ;@@B    @,                                             @;                         r@@h     
	                  @@Hh   3s                                            @@                       ,,S@@@@G    
	                   #@@r  9;                                           @@                     ;@@@@#B#@@r    
	                    @@#, H2                                         3@G                     &@@;     #&     
	                     &@@rG:                                       r@@:                     H@&       Mh     
	                      H@@@#,                                   .M@@@                      :@H        #&     
	                       :#@@@&i,                              ;@@@@X                       @@     ,riX@@9i;. 
	                         ;@@@@@MS:                        ,3@@@Xs@@                      @@      ;ir;,;rsr, 
	                           .5A@@@@@H2;r;,,.::;;:..:r559@@@@@S i   @@s                   #@                  
	                               i@@@@@@@@@@@#@@@@@@@@@@@@@#@M  r.   @@@@3r.             @@                   
	                                 i@#S.,:sB@,    ;#   @@9:  @@#@r .S.#@i@@@@@X.       :@@.                   
	                                   &X      M;    :# &@XX;   @#iA 2H  #    2@@@@2.  :@@H                     
	                                    3@.    :@     @@@#@&2  ,@  A3  XX.@      s@@@@@@@                       
	                                     #@r    @@M#X i@  X@@5 H@   @:  ,MM#        :2i                         
	                                      @@X   .;:@A ;G   ;@@M@@A   @;  #2B@                                   
	                                      @@@i    is  iM    @@G;.@@  ,@r9; ,@@                                  
	                                     :@@@#    @B  r@   ,@&S   @9  ;@G   2@,                                 
	                                     @@s@@5    AG. @.  r@h;   ;@:  A;    @@                                 
	                                    #@  #@#,     33:i  h@A;    @M  ,@     @A                                
	                                   ;@,  r@#S      hH@: r@A2     @   @:    9@                                
	                                   @@   .@Mi       s@@  @@#.    H,  @:     @;                               
	                                  S@,    @#s         iG .@#9    Ai,i@      &@                               
	                                  @@     @@r          32 s@@S  .@#.:@       @;                              
	                                 i@,     @M3rh&5.     .@@rA#@#@#   XG       X#                              
	                                 @@   .rB@@@9B@@@@#@@@  #B    hr   M.       :@                              
	                                ;@  #@@@@@#:,@@@@@M5;    ;2;  .9  hS         @.                             
	                                #@@@@2  ;@s @:             .rh9@5@;          @H                             
	                                SM5     @@i @                  :2@s          #@                             
	                                        @@S M                     X          2@                             
	                                       ;#3s.,                                .M:                            
	
