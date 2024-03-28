import {useEffect,useState} from 'react'
import './App.css';

function App (){

  const[employee , setEmployee]=useState([]);
  const [depts,setDept]=useState([]);
  const[selectDept , setSelectDept] = useState('');

  const fetchEmployee = async()=>{
    try{
      const employee =await fetch('http://127.0.0.1:8000/API/employees/')
      const employeeData = await employee.json();
      setEmployee(employeeData)
      
    }
    catch(error){
      console.error('Error while fetching data',error)
    }
  }

  const fetchDepartment = async()=>{
    try{
      const depts = await fetch('http://127.0.0.1:8000/API/departments/')
      const deptData =await depts.json()
      setDept(deptData)
    }
    catch(error){
      console.log('Error while fetching data',error)
    }
  }

  useEffect(()=>{
    fetchEmployee();
    fetchDepartment();
  },[])
  return (
    <div className='App'>
      <tabel>
        <tr>
          <th>Name</th>
          <th>Salary</th>
          <th>Native</th>
          <th>Department</th>
        </tr>
        {employee.map((employee , index)=>{
          <tr key={index}>
            <td>{employee.name}</td>
            <td>{employee.salary}</td>
            <td>{employee.native}</td>

            {depts.filter((dept)=>employee.id===employee.dept).map((value,id)=>(
              <td>{value.dept}</td>
            ))}
          </tr>
        })}
      </tabel>
      <select name="Department" value={selectDept} onChange={(e) =>setSelectDept(e.target.value)}>
          <option value="" >All</option>
          {depts.map((dept,index) => (
            <option key={index} value={dept.id}>{dept.dept}</option>
          ))}
        </select>
      
    </div>
  )
}

export default App
