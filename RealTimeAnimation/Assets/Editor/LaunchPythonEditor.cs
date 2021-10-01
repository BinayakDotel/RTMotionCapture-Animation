using System.Collections;
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LaunchPython))]
public class LaunchPythonEditor : Editor
{
	public override void OnInspectorGUI()
	{
		base.OnInspectorGUI();

		LaunchPython launch = (LaunchPython)target;

		if(GUILayout.Button("RUN POSE ESTIMATION", GUILayout.Height(30)))
		{
			launch.CallPython();
		}
	}
}
