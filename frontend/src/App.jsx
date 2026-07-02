import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import PatientSignup from "./pages/PatientSignup";
import PatientLogin from "./pages/PatientLogin";
import DoctorSignup from "./pages/DoctorSignup";
import DoctorLogin from "./pages/DoctorLogin";
import Dashboard from "./pages/Dashboard";

function Home() {
  return (
    <div style={{ maxWidth: 400, margin: "60px auto", textAlign: "center" }}>
      <h1>Doctor Appointment Platform</h1>
      <p><Link to="/signup/patient">Patient Signup</Link></p>
      <p><Link to="/login/patient">Patient Login</Link></p>
      <p><Link to="/signup/doctor">Doctor Signup</Link></p>
      <p><Link to="/login/doctor">Doctor Login</Link></p>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup/patient" element={<PatientSignup />} />
        <Route path="/login/patient" element={<PatientLogin />} />
        <Route path="/signup/doctor" element={<DoctorSignup />} />
        <Route path="/login/doctor" element={<DoctorLogin />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}