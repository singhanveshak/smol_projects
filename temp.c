void CTrampDlg::LoadConfigFile()
{
int handle,ptr;
unsigned long size;
char cfgfile[255];GetModuleFileName(NULL,configpath,254);configpath[ptr]=0;sprintf(cfgdata.listpath,"%s",configpath);sprintf(cfgdata.skinpath,"%s\\skins\\tramp",configpath);
	sprintf(cfgdata.songpath,"%s",configpath);
    
    sprintf(cfgdata.currentskin,"tramp.skn");
    cfgdata.currentsong[0]=0;
	cfgdata.currentlist[0]=0;
	sprintf(cfgfile,"%s\\trampcfg.dat",configpath);

    cfgdata.x=100; cfgdata.y=100;
	cfgdata.w=500; cfgdata.h=175;
for(ptr=0; ptr<11; ptr++) cfgdata.eqpos[ptr]=50;cfgdata.shufflecode=cfgdata.loopcode=false;cfgdata.eqonoff=true;cfgdata.volume=(unsigned long) 0x3fff3fffL;for(ptr=0; ptr<50; ptr++) cfgdata.controls[ptr]=0;handle=open(cfgfile,O_RDWR|O_BINARY);
if(handle==-1) {SaveConfigFile(); return;}
  size=filelength(handle);
 if(size!=sizeof(CONFIGDATA))
  { close(handle);
SaveConfigFile();}
 read(handle,&cfgdata,sizeof(CONFIGDATA));
 close(handle);}