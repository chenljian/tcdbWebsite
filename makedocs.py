# -*- coding: utf-8 -*-
import pymongo
import base64

client = pymongo.MongoClient("localhost", 27017)
db = client.db
tcdb = db.tcdb

tcdb.delete_many({})

docs = [{
    "special_recomm": True,
    "news_cover":base64.b64encode(open('./public/assets/images/upload/20170114-1.jpg','rb').read()),
    "category": "newsdynamics",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date":"20170114",
    "title_cn": "数据库专委会蝉联CCF优秀专委",
    "content": "<p>10月16日，中国计算机学会（CCF）数据库专业委员会在成都召开了全体会议，选举新一届专委领导机构。中国人民大学信息学院院长杜小勇当选为新一届数据库专委会主任。</p><p>数据库专业委员会是中国计算机学会下属35个专业委员会之一，于1999年 8月正式成立，现有委员130人。该专委连续多年是中国计算机学会的优秀专业委员会。中国人民大学的学者在该专业委员会拥有重要影响力，信息学院创始人萨师煊教授曾是该专业委员会的前身——中国计算机学会数据库学组的创始人和领导者，王珊教授是该专委会第一任和第二任主任委员。学会秘书处也挂靠在人民大学，孟小峰教授曾长期担任秘书长职务。</p><p>杜小勇院长现任中国计算机学会会士（CCF Fellow），学会常务理事，长期从事数据库领域基础理论与核心技术的研究，曾任国家863计划数据库重大专项专家组组长。</p>"
},
{
	"special_recomm": False,
    "category": "confinfo",
    "source": "CCF大数据专家委员会",
    "title_en": "p1",
    "date":"20160701",
    "title_cn": "第四届CCF大数据学术会议征文延期通知",
    "content": "<p>继2013-2015年成功召开三届CCF大数据学术会议后，第四届CCF大数据学术会议（CCF BigData      2016）将于2016年10月11日至13日在甘肃省兰州市举行。本届会议由中国计算机学会（CCF）主办，CCF大数据专家委员会与兰州大学联合承办。会议将邀请多位院士和国内外大数据领域的顶级专家学者作大会特邀报告，邀请Science编辑部的高级编辑组织以Scientific      Data in Science为主题的高峰论坛，还将组织专题论坛、青年论坛和分会场口头报告等多种形式的学术交流。会议特别设立最佳学术论文奖、最佳应用论文奖和最佳学生论文奖。现面向学术界与产业界征收中英文稿件，<span              style='color: red'>应广大作者的请求，组委会讨论决定将投稿截止日期延至8月1日，欢迎继续关注并踊跃投稿</span>。论文征文范围包括但不限于以下方面：</p>  <p>大数据科学基础理论与方法</p>  <p>大数据系统构架与基础设施</p>  <p>大数据采集与预处理技术</p>  <p>大数据存储管理模型、技术与系统</p>  <p>大数据并行计算模型、框架与系统</p>  <p>主流开源大数据系统优化与应用实践</p>  <p>大数据分析挖掘与智能计算方法与系统</p>  <p>大数据可视分析与计算</p>  <p>大数据共享开放技术方法与标准</p>  <p>大数据隐私与安全保护技术与标准</p>  <p>大数据系统解决方案与工具平台</p>  <p>大数据行业应用</p>  <p>其他与大数据相关的研究问题</p>  <br/> <strong>重要日期：</strong><br/> 投稿截止日期：<strike>2016年7月01日</strike> <span style='color:#ff0000;'>2016年8月01日</span><br/>  录用通知日期：<strike>2016年8月20日</strike> <span style='color:#ff0000;'>2016年9月15日</span><br/>  正稿提交日期：<strike>2016年9月20日</strike> <span style='color:#ff0000;'>2016年9月25日</span><br/> 会议召开日期：2016年10月11日-13日<br/> <br/>  <strong>论文投稿及稿件格式：</strong><br/> 会议官网：http://ccfbigdata2016.lzu.edu.cn<br/>  投稿网站：https://easychair.org/conferences/?conf=ccfbigdata2016<br/> 论文投稿要求：中文论文版面标准A4幅面，  Word或PDF格式，稿件按照《计算机学报》、《计算机研究与发展》等一级学报期刊论文篇幅要求撰写。英文论文版面标准A4幅面，Word或PDF格式，稿件按照IEEE Transactions on Big  Data等期刊论文篇幅和格式要求撰写。<br/> <br/> <strong>论文录用与发表</strong><br/> 会议现面向学术界与产业界进行征文，中英文稿件都收。本次会议录用的中文论文（包括Industry  Track上录用的文章）将根据论文质量推荐到《计算机学报》、《计算机研究与发展》、《电子学报》、《中文信息学报》、《模式识别与人工智能》、《数据采集与处理》、《清华大学学报（自然科学版）》、《南京大学学报（自然科学版）》、《中国科学技术大学学报》、《计算机科学与探索》、《兰州大学学报（自然科学版）》、《计算机科学》、《计算机应用》、《计算机工程与科学》、《大数据》等国内核心期刊的正刊上发表。录用的优秀英文论文将被推荐给国际期刊IEEE  Transactions on Big Data、International Journal of Data Science and Analytics、Interdisciplinary Sciences: Computational  Life Science(SCI)、International Journal of Computational Science and Engineering (EI)、International Journal of Embedded  Systems (EI)和International Journal of High Performance Computing and Networking (EI)。<br/> <br/>  <strong>会议组织机构：</strong><br/> 指导单位：甘肃省工业与信息化委员会、甘肃省科技厅、甘肃省教育厅<br/> 主办单位：中国计算机学会（CCF）<br/> 承办单位：中国计算机学会大数据专家委员会、兰州大学<br/>  协办单位：西北师范大学、兰州交通大学、兰州理工大学、甘肃省大数据产业技术创新联盟<br/> 大会荣誉主席： 李国杰（中科院计算所）<br/> 大会主席：  梅 宏（上海交通大学） <br/>  王 乘（兰州大学）  <br/> 程序主席： 胡 斌（兰州大学）  <br/>  程学旗（中科院计算所） <br/>  王建民（清华大学）  <br/>  黄宜华（南京大学） <br/> 程序副主席：  梅中磊（兰州大学） <br/>  靳小龙（中科院计算所）<br/>  彭绍亮（国防科技大学） <br/> 组委会主席：  马志新（兰州大学） <br/>  张云泉（中科院计算所） <br/>  党建武（兰州交通大学）  <br/> 最佳论文评审委员会主席：王晓阳（复旦大学）<br/>  国际联络主席： 熊 辉（罗格斯大学） <br/>  操龙兵（悉尼科技大学）  <br/> 张晓东（俄亥俄州立大学）  <br/> 吴若蕾（Science期刊）<br/>  财务主席： 刘颂阳（兰州大学）<br/>  出版主席： 高 阳（南京大学）<br/>  王 莉（太原理工大学）<br/>  魏冬青（上海交通大学）<br/>  宣传主席： 刘 淇（中国科技大学） <br/>  杨 婧（中科院计算所）  <br/> <br/> <strong>会议联系信息：</strong><br/> 投稿咨询与支持：顾荣<br/> 邮箱：gurongwalker@gmail.com<br/>  电话：15850682791<br/> <br/> 会务咨询与支持：金鑫<br/> 邮箱：jinxin@lzu.edu.cn<br/> 电话：0931-8912778<br/>"
},
{
	"special_recomm": False,
    "category": "confinfo",
    "source": "深圳大学计算机与软件学院",
    "title_en": "p1",
    "date":"20160430",
    "title_cn": "第33届中国数据库学术会议（NDBC 2016）征文通知",
    "content": "<h3>征文通知</h3><p>第33届中国数据库学术会议（NDBC2016）将于2016年10月14日至16日在广东省深圳市举行。本次会议由中国计算机学会主办，中国计算机学会数据库专业委员会协办，深圳大学承办，由香港中文大学工程学院和佛山科学技术学院特别协办。</p><p>本届会议将主要关注数据库技术所面临的新的挑战问题和研究方向，着力反映我国数据库技术研究的最新进展。本届会议将继续设立“系统演示”主题，并继续开设“研究生论文指导计划”研讨班等。届时还将邀请国内外数据库领域著名专家到会作专题报告。我们诚征数据管理及其应用领域的论文、专题讨论与系统演示报告等。</p><h3>1.征文范围(不限于这些领域)：</h3><p>数据库实现新技术、云计算环境中的数据管理、Web数据管理</p><p>查询处理与查询优化、数据流管理、XML和半结构化数据</p><p>数据仓库和OLAP、近似和非确定性数据库、内容与知识管理</p><p>数据挖掘和知识发现、元数据管理、数据集成和迁移</p><p>嵌入式数据库与移动数据库、并行和分布式数据库系统、特定领域的数据库系统</p><p>数据库自管理、智能用户接口技术、空间和时态数据库系统</p><p>多媒体数据库技术、数据隐私与安全、信息检索与数据库</p><p>物联网数据管理、数据库系统性能评测、新型存储中的数据管理</p><h3>2.投稿要求：</h3><p>1)论文应是未发表的研究成果，应包括中英文题目、中英文摘要、关键词、正文和参考文献。由于论文采用匿名评审，故论文中不能包含任何作者相关信息（如姓名、单位、电子邮件、通信地址、资助项目等）。</p><p>2)论文中英文均可（鼓励中文），用Word排版，论文篇幅一般不超过A4幅面8页。其格式需参考《计算机研究与发展》的投稿要求，可见《计算机研究与发展》网站。</p><p><a href='http://crad.ict.ac.cn/'target='_blank'>http://crad.ict.ac.cn/</a></p><p>3)会议论文均采用网上提交方式，不支持电子邮件提交论文的方式。</p><p>4)投稿网址：<a href='https://easychair.org/conferences/?conf=ndbc2016'target='_blank'>欢迎通过EasyChair投稿</a></p><h3>3.系统演示：</h3><p>本次大会设立系统演示程序（DemonstrationProgram），欢迎大家踊跃投稿。详细信息请见<a href='SubmissionDemo.shtml'class='important'>系统演示征文通知</a>。</p><h3>4.论文出版：</h3><p>会议录用论文将分A辑和B辑出版，论文拟安排在《计算机学报》（正刊）、《计算机研究与发展》（正刊）、《计算机科学与探索》（正刊）、《计算机研究与发展（增刊）》等刊出版。</p><h3>5.重要日期：</h3><p>论文提交截止时间：2016年5月31日</b>&nbsp;&nbsp;&nbsp;&nbsp;论文录用通知时间：2016年6月30日</p><p>排版稿件截止时间：2016年7月7日&nbsp;&nbsp;&nbsp;&nbsp;提交出版社时间：2016年7月15日</p><h3>6.联系方式：</h3><p>会议网站:<a href='http://csse.szu.edu.cn/ndbc2016'target='_blank'>http://csse.szu.edu.cn/ndbc2016</a></p><p>联系人：李荣华</p><p>邮件：<a href='mailto:ndbc2016@szu.edu.cn'>ndbc2016@szu.edu.cn</a>,<a href='mailto:ndbc2016@gmail.com'>ndbc2016@gmail.com</a></p><p>电话：13510721660</p>"
},
{
	"special_recomm": False,
    "category": "confinfo",
    "source": "苏州大学先进数据分析研究中心",
    "title_en": "p1",
    "date":"20160731",
    "title_cn": "The 18th Asia Pacific Web Conference",
    "content": "<p>APWeb 2016 invites papers describing original contributions in all fields of Web Management and related research areas and applications. All submissions should be in English. For every accepted paper it is required that at least one author will attend the conference to present the work. Research topics of interest for APWeb 2016 include, but are not limited to the following areas:</p><table data-sort='sortDisabled'><tbody><tr class='firstRow'><td width='612' valign='top' style='-ms-word-break: break-all;'><p style='text-align: justify; white-space: normal;'><em>* Advanced application of databases</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Cloud computing</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Content management</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Data caching</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Data mining and knowledge discovery</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Data and information quality Control</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Data migration and integration</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Deep Web</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Digital libraries</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Distributed and parallel systems</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Grid computing</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Emerging Web techniques</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Information retrieval</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Mobile computing and data management</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Multidimensional databases and OLAP</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Multimedia systems</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p></td><td width='612' valign='top' style='-ms-word-break: break-all;'><p style='text-align: justify; white-space: normal;'><em>* Parallel and distributed database systems</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Peer-to-peer systems</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Performance and benchmarking</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Query processing and optimization</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Semantic web and web ontology</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Security, privacy and trust</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Sensor networks</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Service-oriented computing</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Spatial and temporal databases</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Stream data processing</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Storage and data access methods</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Web community analysis</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Web search and mining</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Web services</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* Workflow and E-services</em> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p style='text-align: justify; white-space: normal;'><em>* XML and semi-structured data management</em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p></td></tr></tbody></table>"
},
{
	"special_recomm": False,
    "category": "confinfo",
    "source": "四川大学数据库与知识工程研究所",
    "title_en": "p1",
    "date":"20150912",
    "title_cn": "第32届全国数据库学术会议",
    "content": "<p>由数据库专业委员会主办的全国数据库学术会议（NDBC）始于1977年。自1999年数据库专委会成立以来，数据库专委会继承中国数据库界多年来形成的优良传统，致力于办好这一传统的数据库盛会，为中国大陆、香港、台湾、澳门和海外华裔数据库研究者、开发者和用户提供一个大中华数据库论坛，交流有关数据库研究与应用的成果和经验，探讨数据库研究与应用所面临的关键性挑战问题和研究方向，至今已举办31届。在最近几年中，会议收文的数量逐年递增，而论文的录取率却逐年递减，标志着数据库年会影响范围的扩大和论文质量的提高。参加全国数据库学术会议的人数也在增长，近几年来，已经吸引了不少海内外的作者投稿和参会。与此同时，数据库专委会努力扩大国际交流，寻求与国际数据库学术组织的广泛合作，将NDBC逐步与国际接轨，使之成为亚太地区，乃至世界性的有影响力的国际会议。经过几年的努力，我们高兴地看到NDBC正朝着预定的目标稳步前进。</p><img src='assets/images/upload/20150912-1.jpg'>"
},
{
	"special_recomm": False,
    "category": "newsdynamics",
    "source": "中国人民大学信息学院",
    "title_en": "p1",
    "date":"20151024",
    "title_cn": "杜小勇教授当选中国计算机学会数据库专委会主任",
    "content": "<p>10月16日，中国计算机学会（CCF）数据库专业委员会在成都召开了全体会议，选举新一届专委领导机构。中国人民大学信息学院院长杜小勇当选为新一届数据库专委会主任。</p><p>数据库专业委员会是中国计算机学会下属35个专业委员会之一，于1999年 8月正式成立，现有委员130人。该专委连续多年是中国计算机学会的优秀专业委员会。中国人民大学的学者在该专业委员会拥有重要影响力，信息学院创始人萨师煊教授曾是该专业委员会的前身——中国计算机学会数据库学组的创始人和领导者，王珊教授是该专委会第一任和第二任主任委员。学会秘书处也挂靠在人民大学，孟小峰教授曾长期担任秘书长职务。</p><p>杜小勇院长现任中国计算机学会会士（CCF Fellow），学会常务理事，长期从事数据库领域基础理论与核心技术的研究，曾任国家863计划数据库重大专项专家组组长。</p>"
},

{
	"special_recomm": True,
    "news_cover":base64.b64encode(open('./public/assets/images/upload/20160727-1.jpg','rb').read()),
    "category": "newsdynamics",
    "source": "江西财经大学信息学院",
    "title_en": "p1",
    "date":"20160727",
    "title_cn": "2016年中国数据库发展研讨会在南昌成功举办",
    "content": "<p>由中国计算机学会主办，中国计算机学会数据库专业委员会协办，江西财经大学承办的2016年中国数据库发展研讨会暨审稿会于6月2至3日在英雄城南昌隆重召开。国内外数据库领域专家们共聚一堂，分享数据库研究与应用的最新成果和经验，探讨数据库领域的热点问题，交流未来研究方向，中国计算机学会数据库专委委员共80余人参加了本次会议。</p><img src='assets/images/upload/20160727-1.jpg'><p>此次研讨会共分两个环节：数据库发展战略研讨以及专委会工作汇报和讨论。在第一个环节，会议特别邀请了国内外数据库领域五位杰出数据库学者作新技术报告。国际著名数据库专家、新加坡国立大学Ooi Beng Chin教授做了《Musings on Database Research》的主题报告。国内四位优秀数据库学者也分别做主题报告：北京大学崔斌研究员的《大数据实时推荐》、浙江大学陈刚教授的《关于大数据管理系统发展趋势的思考与实践》、哈尔滨工业大学王宏志教授的《大数据清洗的探索与实践》以及北京大学邹磊副教授的《RDF知识图谱数据管理中的开放性问题》。专家学者的报告着眼领域前沿，内容精彩纷呈，得到与会者的好评。</p><img src='assets/images/upload/20160727-2.jpg'><img src='assets/images/upload/20160727-3.jpg'><p>数据库专委会秘书长崔斌研究员主持了会议的第二个环节───专委会工作会议。深圳大学毛睿教授代表NDBC 2016程序委员会报告了NDBC 2016会议的组织情况，四川大学李川副教授对NDBC 2015进行了总结汇报。专委会副主任高宏教授向大家讲解了NDBC章程且就相关问题与专委代表进行了意见的征询与交流讨论。专委会主任杜小勇教授做了专委工作报告，对专委各工作组的设计定位、工作目标进行了介绍，且重点谈及了数据库科学同产业技术的关系、如何推动数据库领域产学研合作等热点问题，鼓励全体专委委员为专委的工作献计献策。会议同时进行了专委会常委的选举，通过无记名投票，选举产生13位专委常委：李青、高军、李国徽、李国良、王宏志，马帅、毛睿、陈刚、钱卫宁、陈红、张志强、尚学群、申德荣。最后，专委会周立柱教授谈及了专委会刊Data Science and Engineering 的运行情况，鼓励各专委委员为专委会刊的建设贡献力量。</p><img src='assets/images/upload/20160727-4.jpg'><img src='assets/images/upload/20160727-5.jpg'><p>会议成功举办，圆满结束。此次会议安排充实、紧凑，既有战略研讨，又有工作讨论，为广大学者展开对话，切磋学问、交流思想、探讨问题，分享经验搭建了良好的学术交流平台。</p>"
},
{
	"special_recomm": False,
    "category": "commdynamics",
    "source": "贵阳网",
    "title_en": "p1",
    "date":"20160512",
    "title_cn": "杜小勇：政府做好大数据治理 必须具备互联网思维",
    "content": "<p>习近平总书记在网络安全和信息化工作座谈会上说：“网信事业代表着新的生产力、新的发展方向，应该也能够在践行新发展理念上先行一步。”</p><p>对此，中国人民大学信息学院院长杜小勇在接受专访时说：“大数据正在成为这个世界上最重要的土壤和基础，成为一切管理和决策的依据。运用新理念、新技术、新方法对大数据进行全生命周期的创新管理和应用，是推动国民经济转型和社会管理创新的重要契机，也是提升国家综合竞争力的重要趋势。”</p><h3>大数据的“大”意味深长</h3><p>“大数据是因信息技术，特别是数据获取技术的革命性进步而形成的信息爆炸现象”。杜小勇认为，大数据是上世纪80年代“信息爆炸”现象的延续，并不是一个新的时代的开始，“我们仍然处于信息时代。‘大’是一个相对的概念。上世纪70年代，要管理数百万条记录的数据就是一个大的挑战。全球的数据量仍然按照摩尔定律的速度在增长，因此，大数据可以看作信息化过程中的必然现象。”</p><p>杜小勇说，大数据因其规模巨大、类型复杂、产生速度快、价值密度低等因素，对现有信息技术产生巨大挑战，需要运用新理念、新技术、新方法对其进行全生命周期的创新管理和应用，从而促进国民经济的转型升级、社会管理的模式更新，乃至国家综合竞争力的全面提升。</p><p>大数据前面有个‘大’，表示它和一般的数据不同。”杜小勇说，数据是用来描述事物的性质和状态的。如果我们把描述某个人的全部可能收集到的数据都收集起来，形成这个人的一条“长长的数字尾巴”，就有点“大数据”的味道了。</p><h3>发展大数据要打破信息孤岛</h3><p>杜小勇表示，在大数据时代，有志于引领组织实现大数据转型的管理者们首先要养成问“数据怎么说”的习惯，重视数据。其次，要允许数据做主，放手让“大数据说话”，这将是改变组织决策文化的最大力量。</p><p>“要养成整合思维、打破信息孤岛的习惯。”杜小勇说，政府掌握着社会方方面面的大数据，人口、交通、卫生、社保、税收、城市规划等。虽然大多数政府部门都建成了比较完备的信息化平台，但是各个部门间的数据没有进行高效整合，大量部门的数据如一个个信息孤岛，给政府调度和公众办事带来了不便，也制约了数据活力的激发。</p><p>“要打破条块分割，实现不同政府部门、不同层级之间数据的集中共享。”杜小勇说，一方面，需进行纵向信息系统整合，在相同的上下级政府部门之间，利用多级网络和中心数据库，构建统一的信息平台。另一方面，还需进行水平的电子政务信息系统整合，实现跨部门的政府信息资源共享和政务协同。例如，在社保（市民）卡办理的时候，以共享信息的方式使用二代身份证照片，可减少市民照相和出行成本等。</p><p>“要彻底打破信息孤岛，还需要从内部管理观念和行政体制上着手。观念和态度不变，即使手握利器，行政效率和服务质量也难提高。”杜小勇说。</p><p>发展大数据的技术和开展以大数据为特征的信息化应用，势在必行。”杜小勇认为，发展大数据，就是要解决人们的核心关注。电商企业用大数据解决用户画像问题，这是企业的核心关注；政府用大数据解决一个治理难题，这是群众的核心关注。</p><p>杜小勇表示，政府要做好大数据治理，必须深入理解互联网思维，这其中包括互关联思维、去中心思维和人本思维。</p><p>“在互关联思维中，通过挖掘海量数据，呈现一个充满关联的世界。在去中心思维中，互联网时代最鲜明的特征是去中心化、平等化。政府的组织形态必将越来越开放，从条块分割、封闭的架构向开放、协同、合作的方向迈进。”杜小勇说，伴随互联网和大数据浪潮而来的，将是一个非线性的、去中心化的、自下而上的、发现群体智慧的决策模式。</p>	<p>他认为，人本思维指的则是政务人性化。“政府的核心职能就是为人民服务，以人为本是贯彻落实科学发展观的核心要求。在这个层面上，我们的执政理念与互联网精神是非常契合的。在大数据的辅助下，政府一方面能够实时、全面感知和预测公众所需的各类服务和信息，及时发现需求热点，为用户提供更加智能化的办事、便民服务；另一方面，对公民需求的多维度多层次细分，把从面上的需求判断变为对需求细节的感知，使政府服务提供更精准、更个性化。”</p>"
},
{
	"special_recomm": False,
    "category": "commdynamics",
    "source": "北京大学信息科学技术学院网络与信息系统研究所、学院科研办公室",
    "title_en": "p1",
    "date":"20160523",
    "title_cn": "网络与信息系统研究所崔斌研究员课题组在大数据实时推荐研发中取得重要进展",
	"content": "<p>随着大数据时代的来临，从海量信息中迅速获取有用信息的需求日益强烈。个性化推荐系统以海量数据挖掘为基础，引导用户发现自己的信息需求，现已在多个领域得到广泛应用。传统上，通过定期分析数据来更新模型，导致推荐模型无法保持实时性，破坏对用户当前行为推荐结果的准确性。而实时个性化推荐系统可以通过实时分析用户产生的数据，更准确地为用户推荐，与此同时，还可以根据实时推荐结果进行反馈，改进推荐模型，提升系统性能。</p><p>北京大学信息科学技术学院网络与信息系统研究所、高可信软件技术教育部重点实验室崔斌研究员课题组与腾讯公司数据平台部从2014年起联合开展大数据实时推荐研发。研究工作针对海量性、实时性、精准性等大数据应用中的实际难点，创新性地同时从系统、数据和算法三方面着手解决，即：系统方面，针对现有系统的不足，提出由实时接入、实时处理和分布式K-V存储三部分组成的系统架构；数据方面，针对现实世界中严重的数据稀疏、隐反馈数据等问题，提出解决方案；算法方面，针对传统机器学习算法难于应对大规模数据实时计算的问题，提出增量计算模型和增量更新方法，有效地实现了分布式流式在线学习。由此研发的实时推荐系统应用于包括视频、新闻等腾讯的多项实际业务，现每天处理千亿条用户行为，支撑百亿级用户请求，推荐效果显著提升，点击率（click-through-rate, CTR）平均提高6%～18%。腾讯大数据日前的官方报道《大数据实时推荐：不只是统计》首日阅读量达上万次。</p><p>上述成果还以题为《TencentRec：实时流推荐的系统实践》（TencentRec: real-time stream recommendation in practice）和《实时视频推荐探索》（Real-time video recommendation exploration）的论文连续两年在美国计算机学会数据管理专业组年会（Association for Computing Machinery Special Interest Group on Management Of Data, ACM SIGMOD）上发表。第一作者均为信息学院博士研究生黄艳香，通讯作者是崔斌研究员。信息学院徐嬴、谢怡然等研究生以及腾讯平台部蒋杰等也参与该研究。</p><p>本研究得到国家自然科学基金、国家重点基础研究发展计划（即“973计划”）和腾讯云计算数据中心的支持。</p>"
},
{
	"special_recomm": True,
    "news_cover":base64.b64encode(open('./public/assets/images/upload/20151027-1.jpg','rb').read()),
    "category": "commdynamics",
    "source": "中国人民大学信息学院",
    "title_en": "p1",
    "date":"20151027",
    "title_cn": "王珊教授团队荣获2015中国计算机学会科技进步一等奖",
	"content": "<p>我国计算机领域的年度盛会——中国计算机大会（China National Computer Congress，CNCC）10月22日在合肥召开。大会由中国计算机学会(CCF)主办，中国人民大学信息学院计算机科学与技术系师生在本次大会上荣获多项奖励，王珊教授及其团队获得2015中国计算机学会科学技术进步奖一等奖。</p><p>王珊教授及其团队的《数据库管理系统核心技术的创新与成果转化》获得2015中国计算机学会科学技术进步奖一等奖。该项目在大型数据库的体系结构、智能数据分析、多类型数据支持等方面取得了一系列创新成果，全面提升了金仓数据库的技术水平，支撑国产数据库在国家重点行业业务中的应用，经济和社会效益显著。</p><img src='assets/images/upload/20151027-1.jpg'><p style='text-align: center'>中国计算机学会理事长郑纬民教授为王珊教授颁奖</p><p>中国计算机大会是国内计算机领域级别最高、规模最大的会议，本年度大会的主题是“互联网催生新经济”，重点探讨计算机及信息科学技术领域最新进展和发展趋势，互联网时代下的经济新格局、新变化等问题。来自国内学术界、产业界、政府部门、媒体界的4000余人参加了本次盛会。中国人民大学计算机科学与技术系在本次大会上荣获多项奖励。</p><p>王珊、王会举、覃雄派、周煊发表在2011计算机学报上的论文《架构大数据：挑战、现状与展望》获得2010-2014中国计算机学报优秀论文奖（共3篇）。该论文自2011年发表以来，目前已被引用四百多次。</p><img src='assets/images/upload/20151027-2.jpg'><p style='text-align: center'>左起：周煊、王珊、王会举、覃雄派</p><p>作为最年轻的演讲者，博士生华雯被特别论坛CNCC Plus遴选为报告人，介绍她发表在数据库领域国际顶级会议的ICDE 2015（中国计算机学会A类期刊会议）论文。在报告中，华雯介绍了计算机如何准确且快速地理解互联网时代的“快餐式”语言，以及这一项技术在语义检索、查询推荐、实体浏览等场景的应用。</p><img src='assets/images/upload/20151027-3.jpg'><p style='text-align: center'>博士生华雯在特别论坛CNCC Plus作报告</p><p>直博一年级新生牛玉磊因在本科期间的卓越成果和优异表现，获得“2015中国计算机学会优秀大学生奖（The CCF Outstanding Undergraduate Award）”。牛玉磊以第一作者身份完成的英文论文被人工智能国际顶级会议IJCAI 2015（中国计算机学会A类期刊会议）全文录用。</p><p>计算机科学与技术系的多位师生参加了本次大会，并与来自海内外的专家学者进行了近距离深层次的交流。</p><img src='assets/images/upload/20151027-4.jpg'><p style='text-align: center'>部分参会教师合影</p><img src='assets/images/upload/20151027-5.jpg'><p style='text-align: center'>参会教师与2014年图灵奖（世界计算机界最高奖）获得者Michael Stonebraker合影</p>"
},
{
    "special_recomm": False,
    "category": "confinfo",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date": "20120220",
    "title_cn": "中国计算机学会第28届中国数据库学术会议总结",
    "content": "<p>由中国计算机学会主办，复旦大学共同承办的第28届中国数据库学术会议(CCF NDBC2011)于10月22日上午在复旦大学逸夫科技楼召开。这是中国数据库界的一次盛会，有来自海外及全国各地的代表300余人参加本次大会，来自90多所大专院校研究机构。</p><p>复旦大学金力副校长代表学校到会致辞，向与会者介绍了复旦大学的发展和现状，并特别介绍了复旦大学数据库方向的基本情况，同时他和结合他自己的研究方向强调了数据库研究方向对其它应用领域的影响和支撑。大会开幕式前，金力副校长会见了老专家代表、大会特邀讲者等。中国计算机学会秘书长、杜子德教授代表中国计算机学会向本届数据库会议的召开表示祝贺。他对数据库专业委员会在学会组织、学术交流等方面的工作进行高度的评价，也祝贺数据库专委多次被评为中国计算机学会优秀专委。中国计算机学会数据库专委会主任、中国工程院院士、北京大学何新贵教授代表专委对来自各方及与本届会议的大力支持表示感谢。何院士指出，数据库专委将本着“团结同行、交流学术、发展学科、培养人才、服务国家”的办会宗旨，继承萨老师的遗志，继续把数据库事业推向新的高度。</p><img src='assets/images/upload/20120220-1.jpg'><p>大会开幕式由本次大会主席、顾宁教授主持。顾宁教授代表会议组织方简要介绍了会议的基本情况。本届会议主要关注数据库技术及其应用领域所面临的新的挑战问题和研究方向，着力反映我国数据库技术研究的最新进展。会议共收有效投稿论文297篇，经过双匿名网络评审，最终录用论文124篇，录用率为41.8%。本次大会的主要活动如下：</p><h3>一、研究生优秀论文指导研讨会。</h3><p>这个活动是在“萨师煊奖励计划”的支持下举办的。在研讨会上来自香港城市大学的李青教授和加拿大SIMON FRASER大学的裴健教授从高水平论文的书写和研究生阶段的学习方法的角度进行了指导。来自香港城市大学的Jeffrey Xu Yu教授和Hong Cheng教授与来自澳大利亚新南威尔士大学林学民教授和张文杰博士对图数据处理的最新研究成果和发展方向进行了介绍。</p><h3>二、大会报告</h3><p>本次会议组织了4个大会报告。分别是：</p><p>1、周立柱：关键词搜索–从浅层万维网走向深度万维网的挑战与解决方案</p><p>2、王海勋：A Graph Database Engine and Computation Platform</p><p>3、Boualem Benatallah：From Services Composition to End users programming</p>  <p>4、Min Wang : Context-Aware Computing: Applications and Challenges</p><h3>三、新技术报告</h3><p>本次会议组织了5个数据库新技术报告。分别是：</p><p>1、Yanlei Diao :A Platform for Scalable Low-Latency Analytics using MapReduce</p>  <p>2、朱扬勇：数据学和数据科学</p><p>3、黄艳 : Towards A Smarter and Greener Transportation System</p><p>4、禹晓辉 : CI-Rank: Ranking Keyword Search Results Based on Collective Importance</p>  <p>5、Lei Chen : Efficient query answering in probabilistic RDF graphs</p><h3>四、企业技术报告</h3><p>EMC、神舟通用数据库、人大金仓三个赞助企业做了企业技术报告，介绍了当前工业界在数据库领域面临的主要问题和相应的解决方案，为数据库领域的基础研究提供了很多新的问题。</p><h3>五、12场分组报告和集中展示</h3><p>本次会议重视参会者的交流与展示，所有论文在十二个分组报告中进行了宣讲，这十二个分组报告的主题是：数据挖掘与知识发现(I,II,III,IV)、查询处理和查询优化(I,II)，空间和时态数据库系统(I,II),数据隐私与安全，多媒体数据库、数据库新技术、web数据管理，近似和非确定性数据库，云计算环境中的数据管理，数据流管理，数据仓库和OLAP，数据库实现新技术，信息检索与数据库(I,II),物联网数据管理。同时会议第一次引进了集中展示的做法，所有的论文宣讲者在三个时间段中以展板的方式与所有的与会者进行交流。这种方式受到了大家的欢迎，每次集中展示中均有大量的老师和同学到场进行交流。</p><h3>六、系统演示</h3>  <p>本次会议上共有26个展示系统进行了演示，最后在评选了3个优秀系统展示论文。<p><p>大会评选出了11篇“萨师煊研究生优秀论文”，在闭幕式上对这些优秀论文进行了奖励。通过这些活动加强了国内数据库领域研究人员之间的交流。<p>  <p>本次会议得到众多企业的慷慨赞助，包括EMC China Lab、HP China Lab、神舟通用、人大金仓、达梦数据库、东软集团、上海豪晟、万达信息、高教出版社、机械工业出版社华章分社、清华出版社等。会议详细信息见http://ndbc2011.fudan.edu.cn/。<p>"
},
{
    "special_recomm": False,
    "category": "commdynamics",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date": "20120422",
    "title_cn": "王珊教授荣获国际数据库会议DASFAA2012杰出贡献奖",
    "content": "<p>2012年4月14-19日在韩国釜山举行的第17届先进应用数据库系统国际会议（DASFAA2012）上，王珊教授荣获本年度大会的杰出贡献奖（Outstanding Contribution Award）。DASFAA是国际数据库领域传统的重要会议，集中了亚太地区杰出的数据库学者。来自20多个国家的近220位学者参加了本次会议。DASFAA每年举办一次，会议包括大会报告（keynote）、研究报告（research sessions）、系统演示（Demo）、辅导报告（tutorial）、研讨会（workshop）等，并设立多个奖项，其中杰出贡献奖（Outstanding Contribution Award）旨在奖励为亚太地区数据库发展做出杰出贡献的资深学者。</p><img src='assets/images/upload/20120422-1.jpg'><p>王珊教授因其在数据库教学、研究和系统开发领域的杰出贡献获得本年度大会的杰出贡献奖。王珊教授长期从事数据库的教学、科研与国际交流。1984-1986年访问美国马里兰大学，参与设计和实现关系数据库系统XDB。1986年回国创立国内首个数据库研究机构--数据工程与知识工程研究所。她与已故萨师煊教授合写的《数据库概论》教材累计印刷200多万册，该书是计算机数据库课程的著名教材，2次获全国优秀教材奖，她带领的团队将该课程打造为国家级精品课程。上世纪末至今，她先后承担数十项国家科研项目，并积极推动数据库技术研发、成果转化和产业化。1999-2007年担任中国计算机学会数据库专委会主任委员，担任多个国际会议主席，促进国内数据库界与国际数据库同行之间的交流，并做出重要贡献。为此大会将本年度杰出贡献奖颁发给王珊教授。这是我国学者首次获此殊荣。颁奖之后，王珊教授应邀作了大会报告，系统介绍了我国数据库发展过程和人民大学在数据库研究和成果应用方面的进展。王珊教授在报告开始特别向已故的恩师萨师煊教授致敬，感谢他对我国数据库事业做出开创性贡献和对自己的培养。</p>"
},
{
    "special_recomm": False,
    "category": "newsdynamics",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date": "20140620",
    "title_cn": "两岸四地大中华数据库高峰论坛在澳门举行",
    "content": "<p>两岸四地大中华数据库高峰论坛（Greater China Database Summit)于2014年6月16日在澳门举办。本次高峰论坛由数据库专委会和WAIM指导委员会共同组织，会议邀请了中国大陆、台湾、香港和澳门的数据库研究领域的40余名专家、学者共同研讨了大数据时代数据库研究的方向、挑战和机遇，推动了两岸四地的在数据库研究领域的合作与交流。</p>"
},
{
    "special_recomm": False,
    "category": "newsdynamics",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date": "20150126",
    "title_cn": "数据库专委会创办的国际学术刊物Data Science and Engineering杂志",
    "content": "<p>由数据库专委会创办的国际学术刊物 Data Science and Engineering 杂志于2015年1月20日上午在清华大学举行了签约仪式。协议由CCF理事长郑纬民教授，Springer副总裁 A. Hoffman先生，南京中新赛克副总经理卢云川，杂志主编李建中和 E. Bertino教授共同签署。DSE杂志由专委会主办，中新赛克全额赞助，Springer采用Open Access （网上在线投稿和评审，录用的论文免费立即在网上发表）方式出版。签约后，杂志尚需完成聘任编委，在线评审与出版平台设置等准备工作，大约八周后将在网上公开亮相，正式征集论文。希望大家通过投稿，大力支持DSE！</p>"
},
{
    "special_recomm": False,
    "category": "newsdynamics",
    "source": "中国计算机学会数据库专委会",
    "title_en": "p1",
    "date": "20130827",
    "title_cn": "中韩数据库技术研讨会在哈尔滨工程大学召开",
    "content": "<p>由中国计算机学会主办、数据库专委会和韩国数据库振兴院协办，哈尔滨工程大学承办的第一届中韩数据库技术研讨会（China-Korea Database Technology Workshop，CKDBTW 2013）于2013年8月16日下午在哈尔滨工程大学启航活动中心隆重召开。这是中韩两国数据库界的首次大型学术交流活动，同时有7家韩国数据库企业举行了韩国数据库技术及产品展览会。本次会议旨在搭建中韩数据库领域之间沟通的桥梁，理论与实践相融合的平台。开展小范围、高层次、务实性的讨论。</p><p>哈尔滨工程大学副校长杨冶教授代表学校到会致辞，向与会代表介绍了哈尔滨工程大学的历史与现状，对中韩两国的数据库专家学者能够相聚在哈尔滨工程大学表示热烈的欢迎，同时祝愿两国的专家学者与相关企业能够通过本次会议深入交流，为今后的深入合作打下坚实的基础。来自中韩两国的50多位代表参加韩国数据技术及产品展览会的剪彩仪式和中韩数据库研讨会开幕式，哈尔滨工程大学杨冶副校长，中国计算机学会数据库专委会主任、清华大学周立柱教授，韩国数据库振兴院徐康洙院长，韩国数据库产业协议会金范常务分别致辞并参加剪彩，哈尔滨工程大学计算机学院印桂生教授主持了剪彩仪式和开幕式。大会开幕式前，杨冶副校长会见了与会的中韩两国专家代表。</p><p>研讨会第一阶段和第二阶段分别由韩国数据库振兴院徐康洙院长和清华大学周立柱教授主持，来自中韩两国的10位讲者做了大会发言。</p><p>最后，韩方代表向哈尔滨工程大学捐赠了数据库软件，哈尔滨工程大学印桂生教授和韩国数据库产业协议会金范常务分别代表中韩双方参加了捐赠仪式。</p>"
},
{
    "special_recomm": False,
    "category": "commdynamics",
    "source": "安徽信息工程学院",
    "title_en": "p1",
    "date": "20150915",
    "title_cn": "中国计算机学会数据库专委会委员、国家教学名师岳丽华教授",
    "content": "<h3>一、个人简介</h3><img src='assets/images/upload/20150915-1.jpg'><p>岳丽华，女，1952年生，教授,现任安徽工程大学机电学院计算机与软件工程系系主任。1975年毕业于中国科学技术大学数学系计算数学专业，1991年获计算机软件工学硕士学位。曾负责过多项数据库管理信息系统的数据库应用开发项目；负责并参加过教育部面向二十一世纪课程教育研究及远程教学网上课程软件研制项目。目前承担国家863项目一项，中科院创新项目两项，国防预研项目一项。作为访问学者，曾到美国佛罗里达大学、东京大学进修访问，是中国计算机学会数据库专委会委员。</p><h3>二、研究方向</h3>   <p>数据库系统及其应用，信息集成，实时数据库</p>   <h3>三、获奖情况</h3>   <p>1、参加研制的“ 微型机关系数据库管理系统”CDB1.0和CDB2.0软件获1990年北京地区优秀软件一等奖；</p><p>2、参加研制的“北京医用低温设备厂MIS系统”获中科院科技进步三等奖（1989）；</p>   <p>3、“大学综合教学管理系统”(项目负责人)，该成果获安徽省教学成果二等奖（1989）；</p><p>4、“电视新闻管理系统”(软件负责人)，该成果获广电部计算机应用成果三等奖（1995）。</p><h3>四、主要论著  </h3>   <p>[1]《数据库系统概论》 岳丽华 丁卫群 科学出版社2000年</p>   <p>[2]《软件技术基础》 岳丽华 纪金龙 黄刘生 中国科技大学出版社1994年</p>   <p>[3]《Delphi程序员指南》岳丽华 杨寿保 薛强（译）科学出版社1997年</p>   <p>[4]“改进的Naive-Bayes方法” 张晓引 岳丽华 中国科学技术大学学报Vol.29,No1 1999</p>   <p>[5]“时序模式算法研究“ 蔡智 岳丽华 王煦法 计算机研究与发展Vol.37，No9 2000</p>   <p>[6]“利用CORBA技术解决数据库访问瓶颈问题” 岳丽华 孙林 微计算机应用2002，Vol.23，No.1，</p><p>[7]“ 时态数据的一种周期函数模式发现研究“ 蔡智 岳丽华 蔡庆生 兰州大学学报（自然科学版）Vol.35 Aug,1999</p><p>[8]“Dynamic Data Distribution Algorithm Based on Behavior Model”Yue lihua Yang xiaoyu Dong qunfeng　2nd International Workshop on Intelligent Multimedia Computing and Networking March 8-12,2002 Durham NC USA</p>"
}]

for doc in docs:
    tcdb.insert(doc)
