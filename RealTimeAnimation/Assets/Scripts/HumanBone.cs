using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HumanBone : MonoBehaviour
{
	public static HumanBone _instance;
	public static HumanBone Instance
	{
		get
		{
			return _instance;
		}
	}

	public Transform[] Bone;

	public void Awake()
	{
		//DontDestroyOnLoad(this);
		if (FindObjectsOfType(GetType()).Length > 1)
		{
			Destroy(gameObject);
		}
		_instance = this;
	}
}
