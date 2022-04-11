using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public Rigidbody rb;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void FixedUpdate()
    {
        int xdirection = 0;
        int zdirection = 0;

           if (Input.GetKey("d"))
            xdirection = 1;
        else if (Input.GetKey("a"))
            xdirection = -1;

        if (Input.GetKey("w"))
            zdirection = 1;
        else if (Input.GetKey("s"))
            zdirection = -1;

        rb.AddForce(xdirection * 1000 * Time.deltaTime, 0, zdirection * 1000 * Time.deltaTime);

    }




}
