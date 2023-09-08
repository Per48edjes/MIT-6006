import Data.Function.Memoize (memoize)
import qualified Data.Vector as V
import Lib (canWin, x)
import Test.Hspec (Spec, describe, hspec, it, shouldBe)

main :: IO ()
main = hspec spec

spec :: Spec
spec = do
    describe "Can she win?" $ do
        it "Detect campaigning can result in win" $
            let ds = V.fromList [12, 4, 7, 50]
                zs = V.fromList [3, 3, 3, 15]
             in canWin zs ds `shouldBe` True

        it "Detect campaigning cannot result in win" $
            let ds = V.fromList [8, 6, 9, 2, 3, 1, 9, 4]
                zs = V.fromList [1, 0, 1, 0, 0, 0, 4, 1]
             in canWin zs ds `shouldBe` False

    describe "How many delegates will campaigning maximally yield?" $ do
        it "Calculate maximum delegates possible in win" $
            let ds = V.fromList [12, 4, 7, 50]
                zs = V.fromList [3, 3, 3, 15]
             in memoize (x zs ds) 0 `shouldBe` 68

        it "Calculate maximum delegates possible for futile campaigning" $
            let ds = V.fromList [8, 6, 9, 2, 3, 1, 9, 4]
                zs = V.fromList [1, 0, 1, 0, 0, 0, 4, 1]
             in memoize (x zs ds) 0 `shouldBe` 21
