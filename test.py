import { useState } from "react";

const App = () => {
  const [firstSelect, setFirstSelect] = useState("adv");

  return (
    <div>
      <label>
        First Select:
        <select value={firstSelect} onChange={(e) => setFirstSelect(e.target.value)}>
          <option value="adv">ADV</option>
          <option value="sw">SW</option>
        </select>
      </label>

      <label>
        Second Select:
        <select>
          {firstSelect === "adv" ? (
            <>
              <option value="adv1">Advanced 1</option>
              <option value="adv2">Advanced 2</option>
              <option value="adv3">Advanced 3</option>
            </>
          ) : (
            <>
              <option value="sw1">Software 1</option>
              <option value="sw2">Software 2</option>
              <option value="sw3">Software 3</option>
            </>
          )}
        </select>
      </label>
    </div>
  );
};

export default App;
