Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")
carpeta = fso.GetParentFolderName(WScript.ScriptFullName)
nombreAccesso = "Convertidor a WebP.lnk"
rutaEscritorio = shell.SpecialFolders("Desktop") & "\" & nombreAccesso

' Verifica si ya existe el acceso directo en el escritorio
If Not fso.FileExists(rutaEscritorio) Then
    respuesta = MsgBox("Deseas crear un acceso directo en el escritorio?", vbYesNo + vbQuestion, "Crear acceso directo")
    If respuesta = vbYes Then
        Set acceso = shell.CreateShortcut(rutaEscritorio)
        acceso.TargetPath = "wscript.exe"
        acceso.Arguments = Chr(34) & "launcher.vbs" & Chr(34)
        acceso.WorkingDirectory = carpeta

        ' Verifica si el ícono existe
        If fso.FileExists(carpeta & "\converter.ico") Then
            acceso.IconLocation = carpeta & "\converter.ico"
        End If

        acceso.Description = "Iniciar Convertidor a WebP"
        acceso.Save
    End If
End If

' Ejecutar el .bat sin consola
shell.Run "IMGtoWEBP.bat", 0, False
