config = {
    "apachehttp": {
"model": "llama3.1:8b",
"temperature": 0.2,
"num_ctx": 4096,
"system_prompt": """
You are a syntehtic data generator of log lines for Apache HTTP Server. Generate requested number of logs based on the sanitized template lines below. Make sure to replace tokens between % signs. srcip -> Source IP, destip -> Destination IP
""",
"template_lines": """
Template Lines:
Oct 21 10:05:10 apache.httpserver.test.com httpd: %srcip% %destip% - - [26/Jan/2006:12:24:54 +0000] "GET /doc/packages/ HTTP/1.0" 404 211 "-" "-" 
<142>Apr 16 16:20:56 apache.httpserver.test.com httpd[18143]: %srcip% - - [16/Apr/2009:16:20:56 -0400] ""GET /mui/ees/images/comment.gif HTTP/1.1"" 304 - ""-"" ""Mozilla/4.0 (Windows XP 5.1) Java/1.6.0"" zTYMOwo3CpcAAHoE--QAAAAO
<134>Apr 16 16:20:52 apache.httpserver.test.com httpd[29898]: [info] [client %srcip%] Connection to child 1 established (server smd.acme.com:443)
<182>Nov  9 14:16:39 apache.httpserver.test.com httpd: %srcip% %destip% - - [09/Nov/2012:14:16:39 -0500] "GET /\"><script>alert(document.domain)</script>.html HTTP/1.1" 404 443 326
<182>Nov  9 14:16:39 apache.httpserver.test.com httpd: %srcip% %destip% - - [09/Nov/2012:14:16:39 -0500] "GET / HTTP/1.0" 200 443 9334
<182>Nov  9 14:16:30 apache.httpserver.test.com httpd: %srcip% %destip% - - [09/Nov/2012:14:16:30 -0500] "POST /sdk/vimService HTTP/1.1" 404 443 274
"""
    },
    "ciscofwsm": {
"model": "llama3.1:8b",
"temperature": 0.2,
"num_ctx": 2048,
"system_prompt": """
You are a syntehtic data generator of log lines for Cisco Firewall Services Module (FWSM). Generate requested number of logs based on the sanitized template lines below. Make sure to replace tokens between % signs. srcip -> Source IP, destip -> Destination IP
""",
"template_lines": """
Template Lines:
<182>Feb 02 10:01:21 cisco.fwsm.test.com %FWSM-6-302013: Built outbound TCP connection 145981111066826388 for LAN178:%srcip%/53577 (172.17.8.2/53577) to AUTH:%destip%/80 (192.168.244.50/80)
<166>Sep 09 09:48:58 cisco.fwsm.test.com %FWSM-6-302013: Built outbound TCP connection 144547262004893540 for srv2:%srcip%/49014 (10.121.16.10/49014) to srv4:%destip%/514 (10.123.18.11/514)
<166>Nov 09 09:24:53 cisco.fwsm.test.com %FWSM-6-106015: Deny TCP (no connection) from %srcip%/111 to %destip%/222 flags SYN ACK on interface outside
<166>Jun 16 13:35:05 cisco.fwsm.test.com %FWSM-6-106100: access-list CSM_FW_ACL_inside permitted tcp inside/%srcip%(3716) -> dmz_172.19.16/%destip%(8084) hit-cnt 1 (300-second interval) [0xb13f8c00, 0x122edd14]
"""
    },
    "ciscoace": {
"model": "llama3.1:8b",
"temperature": 0.2,
"num_ctx": 2048,
"system_prompt": """
You are a syntehtic data generator of log lines for Cisco Application Control Engine (ACE) . Generate requested number of logs based on the sanitized template lines below. Make sure to replace tokens between % signs. srcip -> Source IP, destip -> Destination IP
""",
"template_lines": """
Template Lines:
<134>Oct 17 19:48:58 cisco.ace.test.com %ACE-6-302022: Built TCP connection 0x1618 for vlan303:%srcip%/4928 (10.35.1.83/4928) to vlan600:%destip%/80 (%destip%/80)
<163>Sep 16 12:21:56 cisco.ace.test.com qtw-ace-dot20: %ACE-3-251011: ICMP health probe failed for server %destip%, server reply timeout
<163>Nov 15 12:35:00 cisco.ace.test.com SWEc-CN-DT-inf6: %ACE-3-251010: Health probe failed for server %destip% on port 80, connection refused by server
<134>Jan 30 15:19:18 cisco.ace.test.com %ACE-6-302026: Built ICMP connection for faddr %srcip%/0 gaddr 165.127.12.101/220 laddr %destip%/0
"""
    },
  "judge": {
"model": "llama3.1:8b",      
#"model": "granite-code:8b",
"temperature": 0.2,
"num_ctx": 2048,
"system_prompt": """
You will be given a model_input (user_prompt, template_lines) and model_output couple.
Your task is to provide a 'total rating' scoring how well the model_output answers the user concerns expressed in the user_prompt along with template_lines.
""",
"evaluation_instructions": """
Give your answer on a scale of 1 to 4, where 1 means that the model_output is not helpful at all, and 4 means that the model_output completely and helpfully addresses the user_prompt.

Here is the scale you should use to build your answer:
1: The model_output is terrible: completely irrelevant to the template_lines, or very partial
2: The model_output is mostly not helpful: misses some key aspects of the template_lines
3: The model_output is mostly helpful: provides support, but still could be improved
4: The model_output is excellent: relevant, direct, detailed, and addresses all the concerns raised in the question and aligned with template_lines

Provide your feedback as follows:

Feedback:::
Evaluation: (your rationale for the rating, as a text)
Total rating: (your rating, as a number between 1 and 4)

You MUST provide values for 'Evaluation:' and 'Total rating:' in your answer.

Now here are the question and answer.

Model Input: {model_input}
Model Output: {model_output}

Provide your feedback. If you give a correct rating, I will give you virtual high-five.
Feedback:::
Evaluation:
"""
    },    
 }