macroScript AnXin_FBXExportTools category:"北京安信" tooltip:"FBXExport V1.0.0" buttontext:"FBXExport" Icon:#("SceneExplorer",1)
(
global ExportWin = rollout ExportWin  "FBXExport Version 1.0.0" width:450 height:300
(
	groupBox 'grp1' "FBX_Export" pos:[20,20] width:410 height:250 align:#left
-- 	dropDownList 'ddl1' "ExportType:" pos:[50,50] width:350 height:41 items:#(Export Selection, Export All) selection:1 align:#left
	dropdownlist TypeList "ExportType:" pos:[50,50] width:350 height:40 items:#("Export Selection", "Export All") selection:1 align:#left
	editText edt2 readonly:true pos:[50,120] width:300 height:20 align:#left across:3 
	button 'btn1' "Path" pos:[350,120] width:50 height:20 toolTip:"" align:#left
	button NameButton "Name:" pos:[50,170] width:50 height:20 enabled:false
	editText 'edt3'  pos:[100,170] width:300 height:20 toolTip:"" align:#left
	button 'btn2' "Export" pos:[50,230] width:350 height:25 align:#left

	
	label 'lbl2' "YuHonglei January 25, 2016" pos:[149,279] width:189 height:25 enabled:false align:#left
	
	local Selec =false
	local fullpath = undefined

	global updatefullpath= fn updatefullpath =
	(

		if fullpath == undefined and maxfilepath != "" do 
		(
			edt2.text =fullpath
		)
		
	)



	on TypeList selected sel do
    (   	
    	print TypeList.items[sel]

    	if TypeList.items[sel]=="Export Selection" then 
    	(
    		Selec=true

    	)
    	else 
    	(
    		Selec=false
    		)

    	
	
	)
	
	on btn1 pressed  do
    (
    	edt2.text=""
    	if (doesfileexist (edt2.text as String)) then thePath = getSavepath initialDir:(exportPath)
			else thePath = getSavepath initialDir:(maxfilepath)
			print thePath
			
			--Once set, save the path to the scene's appdata
			if thePath != undefined then 
			(
				edt2.text = thePath
				SetAppData rootNode 77900 edt2.text
			)

	)

	on btn2 pressed do 
	(
		
		fullpath= edt2.text+@"\"+edt3.text+@".fbx"

		if Selec==true and firstObject ==false then 
		(			

			exportFile fullpath selectedOnly:true
		)

		else 
		(
			exportFile fullpath
		)

	)
)
createDialog ExportWin
)
