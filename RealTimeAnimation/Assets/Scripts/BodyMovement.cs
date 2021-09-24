using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BodyMovement : MonoBehaviour
{
	[SerializeField] Transform[] positions;
	[SerializeField] GameObject Body;

	public void Start()
	{
		Body = this.gameObject;
	}

	public void Update()
	{
		if (Input.GetKeyUp(KeyCode.A))
		{
		}
	}
    private void drawWay(Vector3 point1, Vector3 point2)
    {
        
    }
}
