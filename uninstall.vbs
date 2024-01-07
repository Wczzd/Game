Const DeleteReadOnly = True
Set objFSO = CreateObject("Scripting.FileSystemObject")
objFSO.DeleteFile("alien_invasion\*.*"), DeleteReadOnly
strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colSubfolders2 = objWMIService.ExecQuery _
("Associators of {Win32_Directory.Name='" & "alien_invasion" & "'} " _
& "Where AssocClass = Win32_Subdirectory " _
& "ResultRole = PartComponent")
For Each objFolder2 in colSubfolders2
objFSO.deleteFolder objFolder2.name , DeleteReadOnly
Next
