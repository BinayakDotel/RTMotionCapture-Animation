using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using UnityEngine.Animations.Rigging;

public class BodyMovement : MonoBehaviour
{
	public static BodyMovement _instance;
	public static BodyMovement Instance
	{
		get
		{
			return _instance;
		}
	}
	public bool running;
	[SerializeField] int units;

	[SerializeField] Transform[] MovingPoints;
	[SerializeField] LineRenderer line;
	[SerializeField] Transform[] joint;

	[Serializable]
	public class KeyPoints
	{
		public string name;
		public float x;
		public float y;
		public float z;
	}
	public KeyPoints[] ReceivedJoints;

	//For smooth interpolation between keypoints
	[SerializeField] float smooth;

	//For making the movement more sensitive
	[SerializeField] Vector3[] moveSensitivity;
	[SerializeField] string currentKeypoint;

	[SerializeField] float[] rot_angle;

	[SerializeField] HumanBone boneRenderer;
	
	//Index of all the bones whose data is being received
	public enum BoneIndex : int
	{
		NOSE_TIP = 0,
		LEFT_SHOULDER = 1,
		RIGHT_SHOULDER = 2,
		LEFT_WRIST_ROT = 3,
		RIGHT_WRIST_ROT = 4,
		LEFT_WRIST = 5,
		RIGHT_WRIST = 6,
		LEFT_HIP = 7,
		RIGHT_HIP = 8,
		LEFT_ANKLE = 9,
		RIGHT_ANKLE = 10,
		LEFT_FOOT = 11,
		RIGHT_FOOT = 12,
		LEFT_EAR = 13,
		RIGHT_EAR = 14,
	}
	//For Keeping track of every bones in the human model
	public enum BoneRendererIndex : int
	{
		PELVIC = 0,
		NOSE_TIP = 44,
		HEAD_ROTATE= 73,
		LEFT_SHOULDER = 21,
		RIGHT_SHOULDER = 51,
		SPINE_ROTATE = 72,
		LEFT_ARM =22,
		RIGHT_ARM = 52,
		LEFT_ELBOW = 23,
		RIGHT_ELBOW = 53,
		LEFT_WRIST = 24,
		RIGHT_WRIST = 54,
		LEFT_HIP = 1,
		RIGHT_HIP = 7,
		HIP_ROTATE = 71,
		LEFT_ANKLE = 3,
		RIGHT_ANKLE = 9,
		LEFT_FOOT = 4,
		RIGHT_FOOT = 11,
	}
	public void Awake()
	{
		//DontDestroyOnLoad(this);
		if (FindObjectsOfType(GetType()).Length > 1)
		{
			Destroy(gameObject);
		}
		_instance = this;
		//boneRenderer = GameObject.Find("Toon").GetComponent<BoneRenderer>();
		boneRenderer = GameObject.Find("HumanBone").GetComponent<HumanBone>();
	}
	// Start is called before the first frame update
	public void Start()
	{
		MovingPoints[(int)BoneIndex.NOSE_TIP].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.NOSE_TIP].transform.position;

		MovingPoints[(int)BoneIndex.LEFT_FOOT].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_FOOT].transform.position;
		MovingPoints[(int)BoneIndex.RIGHT_FOOT].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_FOOT].transform.position;

		MovingPoints[(int)BoneIndex.LEFT_WRIST].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_WRIST].transform.position;
		MovingPoints[(int)BoneIndex.RIGHT_WRIST].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_WRIST].transform.position;
		
		MovingPoints[(int)BoneIndex.LEFT_WRIST_ROT].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_WRIST].transform.position;
		MovingPoints[(int)BoneIndex.LEFT_WRIST_ROT].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_WRIST].transform.position;
		MovingPoints[(int)BoneIndex.LEFT_SHOULDER].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_SHOULDER].transform.position;
		MovingPoints[(int)BoneIndex.RIGHT_SHOULDER].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_SHOULDER].transform.position;

		MovingPoints[(int)BoneIndex.LEFT_HIP].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_HIP].transform.position;
		MovingPoints[(int)BoneIndex.RIGHT_HIP].transform.position = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_HIP].transform.position;
	}
	public void HeadControl(string name, Vector3 pos, int index)
	{
		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
					new Vector3(pos.x * moveSensitivity[index].x,
								pos.y * moveSensitivity[index].y,
								pos.z * moveSensitivity[index].z), smooth);


		if (name == "LEFT_EAR" || name == "RIGHT_EAR")
		{
			float x = (MovingPoints[(int)BoneIndex.LEFT_EAR].position.x + MovingPoints[(int)BoneIndex.RIGHT_EAR].position.x) / 2;
			float y = boneRenderer.Bone[(int)BoneRendererIndex.HEAD_ROTATE].position.y;
			float z = boneRenderer.Bone[(int)BoneRendererIndex.HEAD_ROTATE].position.z;

			boneRenderer.Bone[(int)BoneRendererIndex.HEAD_ROTATE].position = Vector3.Lerp(boneRenderer.Bone[(int)BoneRendererIndex.HEAD_ROTATE].position,
						new Vector3(x, y, z), smooth);
		}
	}
	public void HandControl(string name, Vector3 pos, int index)
	{
		if (name == "RIGHT_WRIST" || name == "LEFT_WRIST")
		{
			if (pos.y < 0.2)
				moveSensitivity[index].y = 4;

			else if (pos.y >= 0.2 && pos.y <= 0.40)
				moveSensitivity[index].y = 2;

			else if (pos.y > 0.40)
				moveSensitivity[index].y = -2;
		}
		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);

		MovingPoints[(int)BoneIndex.LEFT_WRIST_ROT].rotation = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_ELBOW].transform.rotation;
		MovingPoints[(int)BoneIndex.RIGHT_WRIST_ROT].rotation = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_ELBOW].transform.rotation;

		if (name == "LEFT_SHOULDER" || name == "RIGHT_SHOULDER")
		{
			float x = (MovingPoints[(int)BoneIndex.LEFT_SHOULDER].position.x + MovingPoints[(int)BoneIndex.RIGHT_SHOULDER].position.x) / 2;
			float y = boneRenderer.Bone[(int)BoneRendererIndex.SPINE_ROTATE].position.y;
			float z = boneRenderer.Bone[(int)BoneRendererIndex.SPINE_ROTATE].position.z;
			
			boneRenderer.Bone[(int)BoneRendererIndex.SPINE_ROTATE].position = Vector3.Lerp(boneRenderer.Bone[(int)BoneRendererIndex.SPINE_ROTATE].position,
						new Vector3(x, y, z), smooth);
		}
	}
	public void LegControl(Vector3 pos, int index, string name, bool rotateFoot)
	{
		Transform Leg=null;

		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);

		if (rotateFoot)
		{
			if (name == "LEFT_FOOT")
			{
				Leg = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_FOOT];
				index = (int)BoneIndex.LEFT_FOOT;
			}
			if (name == "RIGHT_FOOT")
			{
				Leg = boneRenderer.Bone[(int)BoneRendererIndex.RIGHT_FOOT];
				index = (int)BoneIndex.RIGHT_FOOT;
			}

			rot_angle[index] = Mathf.Atan((Leg.position.x - pos.x) / (Leg.position.y - pos.y)) * 180 / Mathf.PI;

			Quaternion currentRotationOfUpperRightLeg = MovingPoints[index].transform.rotation;
			Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(new Vector3(0, rot_angle[index], 0));

			Leg.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
				wantedRotationOfUpperRightLeg, Time.deltaTime * smooth);
		}
	}
	public void HipControl(string name, Vector3 pos, int index)
	{
		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);

		if (name == "LEFT_HIP" || name == "RIGHT_HIP")
		{
			float x = (MovingPoints[(int)BoneIndex.LEFT_HIP].position.x + MovingPoints[(int)BoneIndex.RIGHT_HIP].position.x) / 2;
			float y = boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position.y;
			float z = boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position.z;

			boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position = Vector3.Lerp(boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position,
						new Vector3(x, y, z), smooth);

			float rot = Mathf.Atan((boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position.x - pos.x) / (boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position.y - pos.y)) * 180 / Mathf.PI;

			//Quaternion currentRotation = Quaternion.Euler(Vector3.zero);
			//Quaternion wantedRotation = Quaternion.Euler(new Vector3(0, rot, 0));

			//boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].transform.Rotate(0, rot, 0, Space.Self);

			//boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].rotation = Quaternion.RotateTowards(currentRotation,
				//	wantedRotation, Time.deltaTime );
		}
		/*print("HIP");
		float x = (MovingPoints[(int)BoneIndex.LEFT_HIP].position.x + MovingPoints[(int)BoneIndex.RIGHT_HIP].position.x) / 2;
		float y = (MovingPoints[(int)BoneIndex.LEFT_HIP].position.y + MovingPoints[(int)BoneIndex.RIGHT_HIP].position.y) / 2;
		float z = (MovingPoints[(int)BoneIndex.LEFT_HIP].position.z + MovingPoints[(int)BoneIndex.RIGHT_HIP].position.z) / 2;
		print($"DATA::{x}, {y}, {z}");
		boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position = Vector3.Lerp(boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].position,
					new Vector3(x, y, z), smooth);
		
		*/
		/*float rot = Mathf.Atan((Hip.position.x - pos.x) / (Hip.position.y - pos.y)) * 180 / Mathf.PI;
		rot_angle[(int)BoneRendererIndex.LEFT_HIP] = rot;
		Quaternion currentRotation = MovingPoints[index].transform.rotation;
		Quaternion wantedRotation = Quaternion.Euler(new Vector3(0, rot, 0));

		boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].rotation = Quaternion.RotateTowards(currentRotation,
				wantedRotation, Time.deltaTime * smooth);*/
		//boneRenderer.Bone[(int)BoneRendererIndex.HIP_ROTATE].rotation = boneRenderer.Bone[(int)BoneRendererIndex.LEFT_FOOT].transform.rotation;
	}


	// Update is called once per frame
	void Update()
	{
		if (running && ReceivedJoints.Length > 0)
		{
			try
			{
				int index = 0;

				foreach (KeyPoints data in ReceivedJoints)
				{
					if (data.name == "NOSE_TIP")
						HeadControl(data.name, new Vector3(data.x, data.y, data.z), index);

					if (data.name == "LEFT_EAR" || data.name == "RIGHT_EAR")
						HeadControl(data.name, new Vector3(data.x, data.y, data.z), index);

					if (data.name == "LEFT_SHOULDER" || data.name == "RIGHT_SHOULDER")
						HandControl(data.name, new Vector3(data.x, data.y, data.z), index);

					if (data.name == "LEFT_WRIST" || data.name == "RIGHT_WRIST")
						HandControl(data.name, new Vector3(data.x, data.y, data.z), index);

					if (data.name == "LEFT_ELBOW" || data.name == "RIGHT_ELBOW")
						HandControl(data.name, new Vector3(data.x, data.y, data.z), index);

					if (data.name == "RIGHT_ANKLE" || data.name == "LEFT_ANKLE")
						LegControl(new Vector3(data.x, data.y, data.z), index, data.name, false);

					if (data.name == "LEFT_FOOT" || data.name == "RIGHT_FOOT")
						LegControl(new Vector3(data.x, data.y, data.z), index, data.name, true);

					if (data.name == "LEFT_HIP" || data.name == "RIGHT_HIP")
						HipControl(data.name, new Vector3(data.x, data.y, data.z), index);

					++index;
				}
			}
			catch
			{
				print("WAITING");
			}
		}
	}
}
