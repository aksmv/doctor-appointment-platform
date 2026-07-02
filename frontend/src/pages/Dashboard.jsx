import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();
  const role = localStorage.getItem("role");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <div style={{ maxWidth: 500, margin: "60px auto" }}>
      <h2>Welcome, {role === "doctor" ? "Doctor" : "Patient"}!</h2>
      <p>You're logged in. This is your dashboard.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}