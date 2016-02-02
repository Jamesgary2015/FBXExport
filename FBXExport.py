import maya.cmds as cmds
isAll='Export Selection';
configpath = 'Select Export Folder'
FileName ='aaaa'

def UI():
	if cmds.window('FBXExport',ex=True):
		cmds.deleteUI('FBXExport',wnd=True)
	window = cmds.window('FBXExport',t='FBX Export Version 1.0.0',wh=(450,300),sizeable=False)

	mainLayout = cmds.columnLayout(w=450, h=300)
	cmds.menuBarLayout()
	# cmds.menu(label ='About Me',helpMenu=True)
	cmds.menu(label='File')
	cmds.menuItem(label='About Me',c=AboutMe)
	cmds.menuItem(label='Help',c=Help)
	cmds.separator(st='in')
	cmds.columnLayout(columnAlign='left', columnAttach=('both', 50), rowSpacing=30, columnWidth=420)
	cmds.text(l='')
	cmds.optionMenu(label ='ExportType:',changeCommand=printNewMenuItem)
	cmds.menuItem( label='Export Selection' )
	cmds.menuItem( label='Export All' )
	
	cmds.rowColumnLayout(numberOfColumns=2)
	cmds.textField("filepath",w=270,pht=configpath, bgc=(0.2,0.2,0.2))
	cmds.button(l='path',w =50,h=20,c=browseFilePath)
	cmds.setParent( '..' )

	cmds.rowColumnLayout(numberOfColumns=2)
	cmds.button(l='Name:',w =50,h=20,en=False)
	cmds.textField('FileName',pht='Enter a filename',ed =True,w=270,bgc=(0.2,0.2,0.2))
	cmds.setParent( '..' )
	cmds.button(l='Export',bgc=(0.3,0.7,0.7),c=ExportFBX)

	cmds.showWindow(window)
# def changeName(*args):
# 	FileName = cmds.textField('FileName',q=True,tx=True)
# 	print FileName
def printNewMenuItem( item ):
	global isAll
	# print item
	if item=='Export Selection':
		isAll='Export Selection'
	elif item =='Export All':
		isAll='Export All'
	print isAll
def browseFilePath(*args):
	configpath = cmds.fileDialog2(ds=2,fm=3,cap="Select Export Folder")[0]
	# returnPath =cmds.cmds.fileDialog2(ds=1)
	cmds.textField("filepath", edit=True, text=configpath)
def ExportFBX(*args):
	filePath =cmds.textField('filepath',q=True,tx=True)
	FileName = cmds.textField('FileName',q=True,tx=True)	
	fullpath = filePath+FileName+'.fbx '
	print isAll	
	if isAll=='Export All':
		cmds.file(fullpath,force=True,options="v=1;", typ="FBX export",pr=True,ea=True)
	elif isAll=='Export Selection':
		cmds.file(fullpath,force=True,options="v=1;", typ="FBX export",pr=True,es=True)	
	# cmds.FBXExport(f=True,fullpath)
def AboutMe(*args):
	cmds.confirmDialog(title='About Me',message='Copyright (C) 2016 by YuHonglei \n\n FBXExport    Version: 1.0.0\n Release Date:  February 2, 2016\n There is no restriction to use or modify but its your own risk.\n All Rights Reserved.',button='OK')

def Help(*args):
	cmds.confirmDialog(title ='Help',message = '1.ExportType:The type of set the export:\n --a.Export Selection:Export the selected object\n --b.Export All:Export the All object\n\n 2.Path:Select Export Folder\n\n 3.Name:Enter a filename ',button='OK')
UI()
